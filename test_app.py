import pytest
from dash.testing.application_runners import import_app


# ✅ Test 1: Header exists
def test_header_exists(dash_duo):
    app = import_app("app")  # loads app.py
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Soul Foods Sales Visualiser" in header.text


# ✅ Test 2: Graph exists
def test_graph_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None


# ✅ Test 3: Region filter exists
def test_radio_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")  # ⚠️ must match app.py
    assert radio is not None