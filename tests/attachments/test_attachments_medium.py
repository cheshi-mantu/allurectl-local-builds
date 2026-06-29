import json
import os
import random

import allure
from allure import attachment_type
from conftest import _should_fail


@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _001")
def test_attach_mediumfile_001():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _002")
def test_attach_mediumfile_002():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _003")
def test_attach_mediumfile_003():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _004")
def test_attach_mediumfile_004():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _005")
def test_attach_mediumfile_005():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _006")
def test_attach_mediumfile_006():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _007")
def test_attach_mediumfile_007():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _008")
def test_attach_mediumfile_008():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _009")
def test_attach_mediumfile_009():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _010")
def test_attach_mediumfile_010():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _011")
def test_attach_mediumfile_011():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _012")
def test_attach_mediumfile_012():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _013")
def test_attach_mediumfile_013():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _014")
def test_attach_mediumfile_014():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _015")
def test_attach_mediumfile_015():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _016")
def test_attach_mediumfile_016():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _017")
def test_attach_mediumfile_017():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _018")
def test_attach_mediumfile_018():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _019")
def test_attach_mediumfile_019():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _020")
def test_attach_mediumfile_020():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _021")
def test_attach_mediumfile_021():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _022")
def test_attach_mediumfile_022():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _023")
def test_attach_mediumfile_023():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _024")
def test_attach_mediumfile_024():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _025")
def test_attach_mediumfile_025():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _026")
def test_attach_mediumfile_026():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _027")
def test_attach_mediumfile_027():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _028")
def test_attach_mediumfile_028():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _029")
def test_attach_mediumfile_029():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _030")
def test_attach_mediumfile_030():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _031")
def test_attach_mediumfile_031():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _032")
def test_attach_mediumfile_032():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _033")
def test_attach_mediumfile_033():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _034")
def test_attach_mediumfile_034():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _035")
def test_attach_mediumfile_035():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _036")
def test_attach_mediumfile_036():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _037")
def test_attach_mediumfile_037():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _038")
def test_attach_mediumfile_038():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _039")
def test_attach_mediumfile_039():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _040")
def test_attach_mediumfile_040():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _041")
def test_attach_mediumfile_041():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _042")
def test_attach_mediumfile_042():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _043")
def test_attach_mediumfile_043():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _044")
def test_attach_mediumfile_044():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _045")
def test_attach_mediumfile_045():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _046")
def test_attach_mediumfile_046():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _047")
def test_attach_mediumfile_047():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _048")
def test_attach_mediumfile_048():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _049")
def test_attach_mediumfile_049():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _050")
def test_attach_mediumfile_050():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _051")
def test_attach_mediumfile_051():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _052")
def test_attach_mediumfile_052():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _053")
def test_attach_mediumfile_053():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _054")
def test_attach_mediumfile_054():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _055")
def test_attach_mediumfile_055():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _056")
def test_attach_mediumfile_056():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _057")
def test_attach_mediumfile_057():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _058")
def test_attach_mediumfile_058():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _059")
def test_attach_mediumfile_059():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _060")
def test_attach_mediumfile_060():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _061")
def test_attach_mediumfile_061():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _062")
def test_attach_mediumfile_062():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _063")
def test_attach_mediumfile_063():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _064")
def test_attach_mediumfile_064():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _065")
def test_attach_mediumfile_065():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _066")
def test_attach_mediumfile_066():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _067")
def test_attach_mediumfile_067():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _068")
def test_attach_mediumfile_068():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _069")
def test_attach_mediumfile_069():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _070")
def test_attach_mediumfile_070():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _071")
def test_attach_mediumfile_071():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _072")
def test_attach_mediumfile_072():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _073")
def test_attach_mediumfile_073():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _074")
def test_attach_mediumfile_074():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _075")
def test_attach_mediumfile_075():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _076")
def test_attach_mediumfile_076():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _077")
def test_attach_mediumfile_077():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _078")
def test_attach_mediumfile_078():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _079")
def test_attach_mediumfile_079():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _080")
def test_attach_mediumfile_080():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _081")
def test_attach_mediumfile_081():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _082")
def test_attach_mediumfile_082():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _083")
def test_attach_mediumfile_083():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _084")
def test_attach_mediumfile_084():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _085")
def test_attach_mediumfile_085():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _086")
def test_attach_mediumfile_086():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _087")
def test_attach_mediumfile_087():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _088")
def test_attach_mediumfile_088():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _089")
def test_attach_mediumfile_089():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _090")
def test_attach_mediumfile_090():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _091")
def test_attach_mediumfile_091():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _092")
def test_attach_mediumfile_092():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _093")
def test_attach_mediumfile_093():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _094")
def test_attach_mediumfile_094():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _095")
def test_attach_mediumfile_095():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _096")
def test_attach_mediumfile_096():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _097")
def test_attach_mediumfile_097():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _098")
def test_attach_mediumfile_098():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _099")
def test_attach_mediumfile_099():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending medium attachments")
@allure.story("Attach 'em mid")
@allure.title("Sending 3 Mb attachments or something like that _100")
def test_attach_mediumfile_100():
    if random.choice([True, False]):
        with allure.step("Sending medium 3 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "medium-image.jpg"), name="3 Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

