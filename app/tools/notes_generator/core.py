from app.utils.document_loaders import get_docs
from app.tools.notes_generator.tools import AINotesGenerator
# from app.services.schemas import AIResistantArgs
from app.services.logger import setup_logger
from app.api.error_utilities import LoaderError, ToolExecutorError

logger = setup_logger()

def executor(topic: str,
             page_layout: str,
             direct_text: str,
             file_url: str,
             file_type: str,
             lang: str, 
             verbose=False):
     
    try:
        logger.info(f"Generating docs. from {file_type}")

        if (file_url and file_type):
            logger.info(f"Generating docs. from {file_type}")
            docs = get_docs(file_url, file_type, True)
        else:
            docs = None
        
        # TODO: Adapt to notes generator
        # ai_resistant_args = AIResistantArgs(
        #     assignment=assignment_description,
        #     grade_level=grade_level,
        #     file_type=file_type,
        #     file_url=file_url,
        #     lang=lang
        # )

        #output = AINotesGenerator(args=ai_resistant_args, verbose=verbose).generate_notes(docs)

        logger.info(f"AI-Resistant Notes generated successfully")

    except LoaderError as e:
        error_message = e
        logger.error(f"Error in AI Resistant Notes Generator Pipeline -> {error_message}")
        raise ToolExecutorError(error_message)
    
    except Exception as e:
        error_message = f"Error in executor: {e}"
        logger.error(error_message)
        raise ValueError(error_message)
    
    return output