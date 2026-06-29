import json
import os
import random

import allure
from allure import attachment_type
from conftest import _should_fail

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _001")
def test_attach_bigfile_001():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _002")
def test_attach_bigfile_002():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _003")
def test_attach_bigfile_003():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _004")
def test_attach_bigfile_004():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _005")
def test_attach_bigfile_005():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _006")
def test_attach_bigfile_006():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _007")
def test_attach_bigfile_007():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _008")
def test_attach_bigfile_008():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _009")
def test_attach_bigfile_009():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _010")
def test_attach_bigfile_010():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _011")
def test_attach_bigfile_011():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _012")
def test_attach_bigfile_012():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _013")
def test_attach_bigfile_013():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _014")
def test_attach_bigfile_014():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _015")
def test_attach_bigfile_015():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _016")
def test_attach_bigfile_016():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _017")
def test_attach_bigfile_017():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _018")
def test_attach_bigfile_018():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _019")
def test_attach_bigfile_019():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _020")
def test_attach_bigfile_020():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _021")
def test_attach_bigfile_021():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _022")
def test_attach_bigfile_022():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _023")
def test_attach_bigfile_023():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _024")
def test_attach_bigfile_024():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _025")
def test_attach_bigfile_025():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _026")
def test_attach_bigfile_026():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _027")
def test_attach_bigfile_027():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _028")
def test_attach_bigfile_028():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _029")
def test_attach_bigfile_029():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _030")
def test_attach_bigfile_030():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _031")
def test_attach_bigfile_031():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _032")
def test_attach_bigfile_032():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _033")
def test_attach_bigfile_033():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _034")
def test_attach_bigfile_034():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _035")
def test_attach_bigfile_035():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _036")
def test_attach_bigfile_036():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _037")
def test_attach_bigfile_037():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _038")
def test_attach_bigfile_038():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _039")
def test_attach_bigfile_039():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _040")
def test_attach_bigfile_040():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _041")
def test_attach_bigfile_041():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _042")
def test_attach_bigfile_042():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _043")
def test_attach_bigfile_043():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _044")
def test_attach_bigfile_044():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _045")
def test_attach_bigfile_045():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _046")
def test_attach_bigfile_046():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _047")
def test_attach_bigfile_047():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _048")
def test_attach_bigfile_048():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _049")
def test_attach_bigfile_049():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _050")
def test_attach_bigfile_050():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _051")
def test_attach_bigfile_051():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _052")
def test_attach_bigfile_052():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _053")
def test_attach_bigfile_053():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _054")
def test_attach_bigfile_054():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _055")
def test_attach_bigfile_055():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _056")
def test_attach_bigfile_056():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _057")
def test_attach_bigfile_057():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _058")
def test_attach_bigfile_058():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _059")
def test_attach_bigfile_059():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _060")
def test_attach_bigfile_060():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _061")
def test_attach_bigfile_061():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _062")
def test_attach_bigfile_062():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _063")
def test_attach_bigfile_063():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _064")
def test_attach_bigfile_064():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _065")
def test_attach_bigfile_065():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _066")
def test_attach_bigfile_066():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _067")
def test_attach_bigfile_067():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _068")
def test_attach_bigfile_068():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _069")
def test_attach_bigfile_069():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _070")
def test_attach_bigfile_070():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _071")
def test_attach_bigfile_071():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _072")
def test_attach_bigfile_072():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _073")
def test_attach_bigfile_073():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _074")
def test_attach_bigfile_074():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _075")
def test_attach_bigfile_075():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _076")
def test_attach_bigfile_076():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _077")
def test_attach_bigfile_077():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _078")
def test_attach_bigfile_078():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _079")
def test_attach_bigfile_079():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _080")
def test_attach_bigfile_080():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _081")
def test_attach_bigfile_081():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _082")
def test_attach_bigfile_082():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _083")
def test_attach_bigfile_083():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _084")
def test_attach_bigfile_084():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _085")
def test_attach_bigfile_085():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _086")
def test_attach_bigfile_086():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _087")
def test_attach_bigfile_087():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _088")
def test_attach_bigfile_088():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _089")
def test_attach_bigfile_089():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _090")
def test_attach_bigfile_090():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _091")
def test_attach_bigfile_091():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _092")
def test_attach_bigfile_092():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _093")
def test_attach_bigfile_093():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _094")
def test_attach_bigfile_094():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _095")
def test_attach_bigfile_095():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _096")
def test_attach_bigfile_096():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _097")
def test_attach_bigfile_097():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _098")
def test_attach_bigfile_098():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _099")
def test_attach_bigfile_099():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.feature("Sending big attachments")
@allure.story("Attach 'em big")
@allure.title("Sending 8 Mb attachments _100")
def test_attach_bigfile_100():
    if random.choice([True, False]):
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    if random.choice([True, False]):
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    if random.choice([True, False]):
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    if random.choice([True, False]):
        with allure.step("JSON attach"):
            allure.attach(json.dumps({"first": 1, "second": 2}, indent=2), name="JSON example", attachment_type=attachment_type.JSON)
    if random.choice([True, False]):
        with allure.step("URI list attach"):
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

