import json
import os
import random

import allure
from allure import attachment_type
from conftest import _should_fail

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _001")
def test_attach_smallfile_001():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _002")
def test_attach_smallfile_002():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _003")
def test_attach_smallfile_003():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _004")
def test_attach_smallfile_004():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _005")
def test_attach_smallfile_005():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _006")
def test_attach_smallfile_006():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _007")
def test_attach_smallfile_007():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _008")
def test_attach_smallfile_008():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _009")
def test_attach_smallfile_009():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _010")
def test_attach_smallfile_010():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _011")
def test_attach_smallfile_011():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _012")
def test_attach_smallfile_012():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _013")
def test_attach_smallfile_013():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _014")
def test_attach_smallfile_014():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _015")
def test_attach_smallfile_015():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _016")
def test_attach_smallfile_016():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _017")
def test_attach_smallfile_017():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _018")
def test_attach_smallfile_018():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _019")
def test_attach_smallfile_019():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _020")
def test_attach_smallfile_020():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _021")
def test_attach_smallfile_021():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _022")
def test_attach_smallfile_022():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _023")
def test_attach_smallfile_023():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _024")
def test_attach_smallfile_024():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _025")
def test_attach_smallfile_025():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _026")
def test_attach_smallfile_026():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _027")
def test_attach_smallfile_027():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _028")
def test_attach_smallfile_028():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _029")
def test_attach_smallfile_029():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _030")
def test_attach_smallfile_030():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _031")
def test_attach_smallfile_031():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _032")
def test_attach_smallfile_032():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _033")
def test_attach_smallfile_033():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _034")
def test_attach_smallfile_034():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _035")
def test_attach_smallfile_035():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _036")
def test_attach_smallfile_036():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _037")
def test_attach_smallfile_037():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _038")
def test_attach_smallfile_038():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _039")
def test_attach_smallfile_039():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _040")
def test_attach_smallfile_040():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _041")
def test_attach_smallfile_041():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _042")
def test_attach_smallfile_042():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _043")
def test_attach_smallfile_043():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _044")
def test_attach_smallfile_044():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _045")
def test_attach_smallfile_045():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _046")
def test_attach_smallfile_046():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _047")
def test_attach_smallfile_047():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _048")
def test_attach_smallfile_048():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _049")
def test_attach_smallfile_049():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _050")
def test_attach_smallfile_050():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _051")
def test_attach_smallfile_051():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _052")
def test_attach_smallfile_052():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _053")
def test_attach_smallfile_053():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _054")
def test_attach_smallfile_054():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _055")
def test_attach_smallfile_055():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _056")
def test_attach_smallfile_056():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _057")
def test_attach_smallfile_057():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _058")
def test_attach_smallfile_058():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _059")
def test_attach_smallfile_059():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _060")
def test_attach_smallfile_060():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _061")
def test_attach_smallfile_061():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _062")
def test_attach_smallfile_062():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _063")
def test_attach_smallfile_063():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _064")
def test_attach_smallfile_064():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _065")
def test_attach_smallfile_065():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _066")
def test_attach_smallfile_066():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _067")
def test_attach_smallfile_067():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _068")
def test_attach_smallfile_068():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _069")
def test_attach_smallfile_069():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _070")
def test_attach_smallfile_070():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _071")
def test_attach_smallfile_071():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _072")
def test_attach_smallfile_072():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _073")
def test_attach_smallfile_073():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _074")
def test_attach_smallfile_074():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _075")
def test_attach_smallfile_075():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _076")
def test_attach_smallfile_076():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _077")
def test_attach_smallfile_077():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _078")
def test_attach_smallfile_078():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _079")
def test_attach_smallfile_079():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _080")
def test_attach_smallfile_080():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _081")
def test_attach_smallfile_081():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _082")
def test_attach_smallfile_082():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _083")
def test_attach_smallfile_083():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _084")
def test_attach_smallfile_084():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _085")
def test_attach_smallfile_085():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _086")
def test_attach_smallfile_086():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _087")
def test_attach_smallfile_087():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _088")
def test_attach_smallfile_088():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _089")
def test_attach_smallfile_089():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _090")
def test_attach_smallfile_090():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _091")
def test_attach_smallfile_091():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _092")
def test_attach_smallfile_092():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _093")
def test_attach_smallfile_093():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _094")
def test_attach_smallfile_094():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _095")
def test_attach_smallfile_095():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _096")
def test_attach_smallfile_096():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _097")
def test_attach_smallfile_097():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _098")
def test_attach_smallfile_098():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _099")
def test_attach_smallfile_099():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending small attachments")
@allure.story("Attach 'em small")
@allure.title("Sending 10 kb attachments or something like that _100")
def test_attach_smallfile_100():
    if random.choice([True, False]):
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

