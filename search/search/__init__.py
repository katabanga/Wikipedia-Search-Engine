"""search package initializer."""
import flask


app = flask.Flask(__name__)  # pylint: disable=invalid-name

app.config.from_object('search.config')

app.config.from_envvar('SEARCH_SETTINGS', silent=True)

import search.views  # noqa: E402  pylint: disable=wrong-import-position
import search.model  # noqa: E402  pylint: disable=wrong-import-position
