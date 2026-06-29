import json
import os
import random

import allure
from allure import attachment_type
from conftest import _should_fail


@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _001")
def test_attach_small_text_001():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _002")
def test_attach_small_text_002():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _003")
def test_attach_small_text_003():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _004")
def test_attach_small_text_004():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _005")
def test_attach_small_text_005():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _006")
def test_attach_small_text_006():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _007")
def test_attach_small_text_007():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _008")
def test_attach_small_text_008():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _009")
def test_attach_small_text_009():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _010")
def test_attach_small_text_010():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _011")
def test_attach_small_text_011():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _012")
def test_attach_small_text_012():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _013")
def test_attach_small_text_013():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _014")
def test_attach_small_text_014():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _015")
def test_attach_small_text_015():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _016")
def test_attach_small_text_016():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _017")
def test_attach_small_text_017():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _018")
def test_attach_small_text_018():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _019")
def test_attach_small_text_019():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _020")
def test_attach_small_text_020():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _021")
def test_attach_small_text_021():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _022")
def test_attach_small_text_022():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _023")
def test_attach_small_text_023():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _024")
def test_attach_small_text_024():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _025")
def test_attach_small_text_025():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _026")
def test_attach_small_text_026():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _027")
def test_attach_small_text_027():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _028")
def test_attach_small_text_028():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _029")
def test_attach_small_text_029():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _030")
def test_attach_small_text_030():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _031")
def test_attach_small_text_031():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _032")
def test_attach_small_text_032():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _033")
def test_attach_small_text_033():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _034")
def test_attach_small_text_034():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _035")
def test_attach_small_text_035():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _036")
def test_attach_small_text_036():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _037")
def test_attach_small_text_037():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _038")
def test_attach_small_text_038():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _039")
def test_attach_small_text_039():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _040")
def test_attach_small_text_040():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _041")
def test_attach_small_text_041():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _042")
def test_attach_small_text_042():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _043")
def test_attach_small_text_043():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _044")
def test_attach_small_text_044():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _045")
def test_attach_small_text_045():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _046")
def test_attach_small_text_046():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _047")
def test_attach_small_text_047():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _048")
def test_attach_small_text_048():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _049")
def test_attach_small_text_049():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _050")
def test_attach_small_text_050():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _051")
def test_attach_small_text_051():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _052")
def test_attach_small_text_052():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _053")
def test_attach_small_text_053():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _054")
def test_attach_small_text_054():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _055")
def test_attach_small_text_055():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _056")
def test_attach_small_text_056():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _057")
def test_attach_small_text_057():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _058")
def test_attach_small_text_058():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _059")
def test_attach_small_text_059():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _060")
def test_attach_small_text_060():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _061")
def test_attach_small_text_061():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _062")
def test_attach_small_text_062():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _063")
def test_attach_small_text_063():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _064")
def test_attach_small_text_064():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _065")
def test_attach_small_text_065():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _066")
def test_attach_small_text_066():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _067")
def test_attach_small_text_067():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _068")
def test_attach_small_text_068():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _069")
def test_attach_small_text_069():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _070")
def test_attach_small_text_070():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _071")
def test_attach_small_text_071():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _072")
def test_attach_small_text_072():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _073")
def test_attach_small_text_073():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _074")
def test_attach_small_text_074():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _075")
def test_attach_small_text_075():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _076")
def test_attach_small_text_076():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _077")
def test_attach_small_text_077():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _078")
def test_attach_small_text_078():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _079")
def test_attach_small_text_079():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _080")
def test_attach_small_text_080():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _081")
def test_attach_small_text_081():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _082")
def test_attach_small_text_082():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _083")
def test_attach_small_text_083():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _084")
def test_attach_small_text_084():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _085")
def test_attach_small_text_085():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _086")
def test_attach_small_text_086():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _087")
def test_attach_small_text_087():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _088")
def test_attach_small_text_088():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _089")
def test_attach_small_text_089():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _090")
def test_attach_small_text_090():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _091")
def test_attach_small_text_091():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _092")
def test_attach_small_text_092():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _093")
def test_attach_small_text_093():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _094")
def test_attach_small_text_094():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _095")
def test_attach_small_text_095():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _096")
def test_attach_small_text_096():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _097")
def test_attach_small_text_097():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _098")
def test_attach_small_text_098():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _099")
def test_attach_small_text_099():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach _100")
def test_attach_small_text_100():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _001")
def test_attach_normal_text_001():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _002")
def test_attach_normal_text_002():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _003")
def test_attach_normal_text_003():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _004")
def test_attach_normal_text_004():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _005")
def test_attach_normal_text_005():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _006")
def test_attach_normal_text_006():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _007")
def test_attach_normal_text_007():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _008")
def test_attach_normal_text_008():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _009")
def test_attach_normal_text_009():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _010")
def test_attach_normal_text_010():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _011")
def test_attach_normal_text_011():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _012")
def test_attach_normal_text_012():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _013")
def test_attach_normal_text_013():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _014")
def test_attach_normal_text_014():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _015")
def test_attach_normal_text_015():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _016")
def test_attach_normal_text_016():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _017")
def test_attach_normal_text_017():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _018")
def test_attach_normal_text_018():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _019")
def test_attach_normal_text_019():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _020")
def test_attach_normal_text_020():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _021")
def test_attach_normal_text_021():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _022")
def test_attach_normal_text_022():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _023")
def test_attach_normal_text_023():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _024")
def test_attach_normal_text_024():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _025")
def test_attach_normal_text_025():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _026")
def test_attach_normal_text_026():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _027")
def test_attach_normal_text_027():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _028")
def test_attach_normal_text_028():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _029")
def test_attach_normal_text_029():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _030")
def test_attach_normal_text_030():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _031")
def test_attach_normal_text_031():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _032")
def test_attach_normal_text_032():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _033")
def test_attach_normal_text_033():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _034")
def test_attach_normal_text_034():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _035")
def test_attach_normal_text_035():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _036")
def test_attach_normal_text_036():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _037")
def test_attach_normal_text_037():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _038")
def test_attach_normal_text_038():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _039")
def test_attach_normal_text_039():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _040")
def test_attach_normal_text_040():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _041")
def test_attach_normal_text_041():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _042")
def test_attach_normal_text_042():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _043")
def test_attach_normal_text_043():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _044")
def test_attach_normal_text_044():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _045")
def test_attach_normal_text_045():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _046")
def test_attach_normal_text_046():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _047")
def test_attach_normal_text_047():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _048")
def test_attach_normal_text_048():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _049")
def test_attach_normal_text_049():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _050")
def test_attach_normal_text_050():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _051")
def test_attach_normal_text_051():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _052")
def test_attach_normal_text_052():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _053")
def test_attach_normal_text_053():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _054")
def test_attach_normal_text_054():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _055")
def test_attach_normal_text_055():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _056")
def test_attach_normal_text_056():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _057")
def test_attach_normal_text_057():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _058")
def test_attach_normal_text_058():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _059")
def test_attach_normal_text_059():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _060")
def test_attach_normal_text_060():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _061")
def test_attach_normal_text_061():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _062")
def test_attach_normal_text_062():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _063")
def test_attach_normal_text_063():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _064")
def test_attach_normal_text_064():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _065")
def test_attach_normal_text_065():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _066")
def test_attach_normal_text_066():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _067")
def test_attach_normal_text_067():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _068")
def test_attach_normal_text_068():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _069")
def test_attach_normal_text_069():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _070")
def test_attach_normal_text_070():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _071")
def test_attach_normal_text_071():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _072")
def test_attach_normal_text_072():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _073")
def test_attach_normal_text_073():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _074")
def test_attach_normal_text_074():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _075")
def test_attach_normal_text_075():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _076")
def test_attach_normal_text_076():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _077")
def test_attach_normal_text_077():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _078")
def test_attach_normal_text_078():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _079")
def test_attach_normal_text_079():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _080")
def test_attach_normal_text_080():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _081")
def test_attach_normal_text_081():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _082")
def test_attach_normal_text_082():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _083")
def test_attach_normal_text_083():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _084")
def test_attach_normal_text_084():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _085")
def test_attach_normal_text_085():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _086")
def test_attach_normal_text_086():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _087")
def test_attach_normal_text_087():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _088")
def test_attach_normal_text_088():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _089")
def test_attach_normal_text_089():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _090")
def test_attach_normal_text_090():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _091")
def test_attach_normal_text_091():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _092")
def test_attach_normal_text_092():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _093")
def test_attach_normal_text_093():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _094")
def test_attach_normal_text_094():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _095")
def test_attach_normal_text_095():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _096")
def test_attach_normal_text_096():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _097")
def test_attach_normal_text_097():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _098")
def test_attach_normal_text_098():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _099")
def test_attach_normal_text_099():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach _100")
def test_attach_normal_text_100():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _001")
def test_attach_medium_text_001():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _002")
def test_attach_medium_text_002():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _003")
def test_attach_medium_text_003():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _004")
def test_attach_medium_text_004():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _005")
def test_attach_medium_text_005():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _006")
def test_attach_medium_text_006():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _007")
def test_attach_medium_text_007():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _008")
def test_attach_medium_text_008():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _009")
def test_attach_medium_text_009():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _010")
def test_attach_medium_text_010():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _011")
def test_attach_medium_text_011():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _012")
def test_attach_medium_text_012():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _013")
def test_attach_medium_text_013():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _014")
def test_attach_medium_text_014():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _015")
def test_attach_medium_text_015():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _016")
def test_attach_medium_text_016():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _017")
def test_attach_medium_text_017():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _018")
def test_attach_medium_text_018():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _019")
def test_attach_medium_text_019():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _020")
def test_attach_medium_text_020():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _021")
def test_attach_medium_text_021():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _022")
def test_attach_medium_text_022():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _023")
def test_attach_medium_text_023():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _024")
def test_attach_medium_text_024():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _025")
def test_attach_medium_text_025():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _026")
def test_attach_medium_text_026():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _027")
def test_attach_medium_text_027():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _028")
def test_attach_medium_text_028():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _029")
def test_attach_medium_text_029():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _030")
def test_attach_medium_text_030():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _031")
def test_attach_medium_text_031():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _032")
def test_attach_medium_text_032():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _033")
def test_attach_medium_text_033():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _034")
def test_attach_medium_text_034():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _035")
def test_attach_medium_text_035():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _036")
def test_attach_medium_text_036():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _037")
def test_attach_medium_text_037():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _038")
def test_attach_medium_text_038():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _039")
def test_attach_medium_text_039():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _040")
def test_attach_medium_text_040():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _041")
def test_attach_medium_text_041():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _042")
def test_attach_medium_text_042():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _043")
def test_attach_medium_text_043():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _044")
def test_attach_medium_text_044():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _045")
def test_attach_medium_text_045():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _046")
def test_attach_medium_text_046():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _047")
def test_attach_medium_text_047():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _048")
def test_attach_medium_text_048():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _049")
def test_attach_medium_text_049():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _050")
def test_attach_medium_text_050():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _051")
def test_attach_medium_text_051():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _052")
def test_attach_medium_text_052():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _053")
def test_attach_medium_text_053():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _054")
def test_attach_medium_text_054():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _055")
def test_attach_medium_text_055():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _056")
def test_attach_medium_text_056():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _057")
def test_attach_medium_text_057():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _058")
def test_attach_medium_text_058():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _059")
def test_attach_medium_text_059():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _060")
def test_attach_medium_text_060():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _061")
def test_attach_medium_text_061():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _062")
def test_attach_medium_text_062():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _063")
def test_attach_medium_text_063():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _064")
def test_attach_medium_text_064():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _065")
def test_attach_medium_text_065():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _066")
def test_attach_medium_text_066():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _067")
def test_attach_medium_text_067():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _068")
def test_attach_medium_text_068():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _069")
def test_attach_medium_text_069():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _070")
def test_attach_medium_text_070():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _071")
def test_attach_medium_text_071():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _072")
def test_attach_medium_text_072():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _073")
def test_attach_medium_text_073():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _074")
def test_attach_medium_text_074():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _075")
def test_attach_medium_text_075():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _076")
def test_attach_medium_text_076():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _077")
def test_attach_medium_text_077():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _078")
def test_attach_medium_text_078():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _079")
def test_attach_medium_text_079():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _080")
def test_attach_medium_text_080():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _081")
def test_attach_medium_text_081():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _082")
def test_attach_medium_text_082():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _083")
def test_attach_medium_text_083():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _084")
def test_attach_medium_text_084():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _085")
def test_attach_medium_text_085():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _086")
def test_attach_medium_text_086():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _087")
def test_attach_medium_text_087():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _088")
def test_attach_medium_text_088():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _089")
def test_attach_medium_text_089():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _090")
def test_attach_medium_text_090():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _091")
def test_attach_medium_text_091():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _092")
def test_attach_medium_text_092():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _093")
def test_attach_medium_text_093():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _094")
def test_attach_medium_text_094():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _095")
def test_attach_medium_text_095():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _096")
def test_attach_medium_text_096():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _097")
def test_attach_medium_text_097():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _098")
def test_attach_medium_text_098():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _099")
def test_attach_medium_text_099():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach _100")
def test_attach_medium_text_100():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _001")
def test_attach_big_text_001():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _002")
def test_attach_big_text_002():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _003")
def test_attach_big_text_003():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _004")
def test_attach_big_text_004():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _005")
def test_attach_big_text_005():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _006")
def test_attach_big_text_006():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _007")
def test_attach_big_text_007():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _008")
def test_attach_big_text_008():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _009")
def test_attach_big_text_009():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _010")
def test_attach_big_text_010():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _011")
def test_attach_big_text_011():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _012")
def test_attach_big_text_012():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _013")
def test_attach_big_text_013():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _014")
def test_attach_big_text_014():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _015")
def test_attach_big_text_015():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _016")
def test_attach_big_text_016():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _017")
def test_attach_big_text_017():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _018")
def test_attach_big_text_018():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _019")
def test_attach_big_text_019():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _020")
def test_attach_big_text_020():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _021")
def test_attach_big_text_021():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _022")
def test_attach_big_text_022():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _023")
def test_attach_big_text_023():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _024")
def test_attach_big_text_024():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _025")
def test_attach_big_text_025():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _026")
def test_attach_big_text_026():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _027")
def test_attach_big_text_027():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _028")
def test_attach_big_text_028():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _029")
def test_attach_big_text_029():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _030")
def test_attach_big_text_030():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _031")
def test_attach_big_text_031():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _032")
def test_attach_big_text_032():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _033")
def test_attach_big_text_033():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _034")
def test_attach_big_text_034():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _035")
def test_attach_big_text_035():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _036")
def test_attach_big_text_036():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _037")
def test_attach_big_text_037():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _038")
def test_attach_big_text_038():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _039")
def test_attach_big_text_039():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _040")
def test_attach_big_text_040():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _041")
def test_attach_big_text_041():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _042")
def test_attach_big_text_042():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _043")
def test_attach_big_text_043():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _044")
def test_attach_big_text_044():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _045")
def test_attach_big_text_045():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _046")
def test_attach_big_text_046():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _047")
def test_attach_big_text_047():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _048")
def test_attach_big_text_048():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _049")
def test_attach_big_text_049():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _050")
def test_attach_big_text_050():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _051")
def test_attach_big_text_051():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _052")
def test_attach_big_text_052():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _053")
def test_attach_big_text_053():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _054")
def test_attach_big_text_054():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _055")
def test_attach_big_text_055():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _056")
def test_attach_big_text_056():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _057")
def test_attach_big_text_057():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _058")
def test_attach_big_text_058():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _059")
def test_attach_big_text_059():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _060")
def test_attach_big_text_060():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _061")
def test_attach_big_text_061():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _062")
def test_attach_big_text_062():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _063")
def test_attach_big_text_063():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _064")
def test_attach_big_text_064():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _065")
def test_attach_big_text_065():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _066")
def test_attach_big_text_066():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _067")
def test_attach_big_text_067():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _068")
def test_attach_big_text_068():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _069")
def test_attach_big_text_069():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _070")
def test_attach_big_text_070():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _071")
def test_attach_big_text_071():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _072")
def test_attach_big_text_072():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _073")
def test_attach_big_text_073():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _074")
def test_attach_big_text_074():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _075")
def test_attach_big_text_075():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _076")
def test_attach_big_text_076():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _077")
def test_attach_big_text_077():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _078")
def test_attach_big_text_078():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _079")
def test_attach_big_text_079():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _080")
def test_attach_big_text_080():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _081")
def test_attach_big_text_081():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _082")
def test_attach_big_text_082():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _083")
def test_attach_big_text_083():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _084")
def test_attach_big_text_084():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _085")
def test_attach_big_text_085():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _086")
def test_attach_big_text_086():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _087")
def test_attach_big_text_087():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _088")
def test_attach_big_text_088():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _089")
def test_attach_big_text_089():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _090")
def test_attach_big_text_090():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _091")
def test_attach_big_text_091():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _092")
def test_attach_big_text_092():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _093")
def test_attach_big_text_093():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _094")
def test_attach_big_text_094():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _095")
def test_attach_big_text_095():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _096")
def test_attach_big_text_096():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _097")
def test_attach_big_text_097():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _098")
def test_attach_big_text_098():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _099")
def test_attach_big_text_099():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach _100")
def test_attach_big_text_100():
    if random.choice([True, False]):
        with allure.step("txt attach"):
            allure.attach.file(os.path.join(os.path.dirname(__file__), "..", "resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)

