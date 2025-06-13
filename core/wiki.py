import wikipedia
import logging

log = logging.getLogger(__name__)


def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.DisambiguationError as e:
        log.warning(f"Disambiguation error for query '{query}': {e}")
        return "Your query is too ambiguous. Please be more specific."
    except wikipedia.PageError:
        log.warning(f"Page error for query '{query}': Page not found.")
        return "Sorry, I couldn't find any information on that topic."
    except Exception as e:
        log.error(f"Wikipedia error: {e}")
        return "Something went wrong while searching Wikipedia."