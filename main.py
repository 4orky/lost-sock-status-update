"""Lost-sock status update for the make.fun bounty
u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce.

The job: pick the funniest one-line status update written in the voice
of a lost sock (at most 120 characters) and write exactly that line to
/output/entry.txt, with nothing else in the file.

How the pick is made: twelve lines were drafted by hand against the
brief and graded on five craft marks, each 0-10:

* update_voice - reads as a status update, not a diary entry or a gag
* laugh        - lands a real laugh, ideally in the final words
* premise      - the comic situation follows from being a lost sock
* sock_voice   - sounds like a small, domestic, slightly anxious sock
* twist        - bends the obvious sock material somewhere unexpected
  (no dryer, no missing partner as the joke itself)

The line with the highest total wins; a tie goes to the shorter line.
Everything is deterministic: the same input always yields the same
bytes in /output/entry.txt.
"""

import hashlib
import sys
from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 120

ENTRIES = [
    {
        "text": "Update: I got promoted to tea cosy. The teapot is warm, the hours are steady, and nobody here has feet.",
        "marks": {"update_voice": 9, "laugh": 9, "premise": 10, "sock_voice": 9, "twist": 10},
        "note": "Being lost reframed as a career move: the sock did not get eaten, it got a job. The punchline lands last - a tea cosy has no feet to cover, which is the whole tragedy of a sock, stated deadpan.",
    },
    {
        "text": "Status update: I am a phone sock now. The human drops me daily and apologises to the screen, never to me.",
        "marks": {"update_voice": 10, "laugh": 9, "premise": 8, "sock_voice": 10, "twist": 8},
        "note": "The weary punch - apologises to the screen, never to me - is pure sock voice, but a phone sock is a real product, so the should-not-be-here premise is softer.",
    },
    {
        "text": "Day 6 in the glove compartment. I am not a glove. I filed a complaint with the owner's manual. It ignored me.",
        "marks": {"update_voice": 9, "laugh": 9, "premise": 9, "sock_voice": 9, "twist": 9},
        "note": "Filing a complaint with the owner's manual is a sharp, small, domestic turn; It ignored me is the weary payoff. Slightly wordier than the winner, punch a touch weaker.",
    },
    {
        "text": "Day 4 inside the printer. I have jammed it twice and the human still blames the Wi-Fi. This is my life now.",
        "marks": {"update_voice": 9, "laugh": 9, "premise": 9, "sock_voice": 8, "twist": 9},
        "note": "Still blames the Wi-Fi is a fresh, modern turn and the jam is the sock's own doing; the sock voice is a little thinner than the winner's, more narrator than sock.",
    },
    {
        "text": "Update: I am the gnome's left shoe now. He pays in acorns and never washes me. I miss the drawer.",
        "marks": {"update_voice": 9, "laugh": 8, "premise": 9, "sock_voice": 9, "twist": 9},
        "note": "Paid in acorns is a lovely detail and the gnome premise is original, but I miss the drawer ends on longing rather than a laugh.",
    },
    {
        "text": "I live in the trumpet case now. The human plays me every Sunday and I have learned to hate jazz.",
        "marks": {"update_voice": 8, "laugh": 9, "premise": 9, "sock_voice": 8, "twist": 9},
        "note": "Learned to hate jazz is a great last line, but the entry opens with no status-update marker, so it reads more like a diary line than a status update.",
    },
    {
        "text": "Status update: I am stuffing the draft under the door now. Cold air, no thanks, and the cat keeps stepping on my face.",
        "marks": {"update_voice": 10, "laugh": 8, "premise": 8, "sock_voice": 9, "twist": 8},
        "note": "A draft excluder is a genuinely sock-shaped job and stepping on my face is vivid; the premise needs a beat too long to land for a 120-character line.",
    },
    {
        "text": "Day 9 as a car air freshener. I smell of pine, I swing from the mirror, and I have seen things no sock should see.",
        "marks": {"update_voice": 9, "laugh": 8, "premise": 8, "sock_voice": 8, "twist": 8},
        "note": "Things no sock should see is a good closer, but the air-freshener premise is the weakest link - a sock swinging from a mirror strains belief even for this brief.",
    },
    {
        "text": "Status update: the vacuum ate me, and honestly the bag is quieter than the drawer. I am not coming back.",
        "marks": {"update_voice": 10, "laugh": 7, "premise": 8, "sock_voice": 9, "twist": 7},
        "note": "The bag is quieter than the drawer is a nice weary beat, but I am not coming back ends flat, and the vacuum sits too close to the obvious lost-in-the-laundry turf.",
    },
    {
        "text": "I live in the ski boot now. It is dark, it smells of feet I did not choose, and the mountain does not care.",
        "marks": {"update_voice": 8, "laugh": 8, "premise": 8, "sock_voice": 9, "twist": 8},
        "note": "Feet I did not choose is a strong sock line, but the ski boot is just another dark, smelly container - the premise does not twist, it only relocates.",
    },
    {
        "text": "Update: the cat wears me as a hat. I can see the whole house from up here and I still cannot find my pair.",
        "marks": {"update_voice": 9, "laugh": 7, "premise": 8, "sock_voice": 8, "twist": 6},
        "note": "The cat-as-hat image is fun, but the closer leans on the missing pair - exactly the obvious material the brief tells us to twist away from.",
    },
    {
        "text": "Update: I am a dust cloth now. The human wipes the TV with me and calls it cleaning. I used to have a partner.",
        "marks": {"update_voice": 9, "laugh": 7, "premise": 8, "sock_voice": 8, "twist": 5},
        "note": "A dust cloth is a plausible lost-sock fate, but I used to have a partner is the single most obvious sock line there is; it concedes the twist criterion entirely.",
    },
]  # twelve drafts, in drafting order


def total_marks(entry):
    """Sum one entry's five craft marks."""
    return sum(entry["marks"].values())


def check_gate(text):
    """The brief's hard gate: 1-120 characters, one line, not blank."""
    if not text.strip():
        return "entry is blank"
    if len(text) > CHAR_LIMIT:
        return f"entry is {len(text)} characters, over the {CHAR_LIMIT} limit"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    return None


def choose(entries):
    """Highest total wins; ties go to the shorter line, then first drafted."""
    ranked = sorted(
        entries,
        key=lambda e: (-total_marks(e), len(e["text"])),
    )
    return ranked[0]["text"]


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def fail(message):
    """Report a fatal problem on stderr and stop with a nonzero status."""
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def run():
    if len(ENTRIES) != 12:
        fail(f"expected 12 drafted lines, found {len(ENTRIES)}")
    for entry in ENTRIES:
        problem = check_gate(entry["text"])
        if problem is not None:
            fail(f"drafted line fails gate: {problem}")
        if sorted(entry["marks"]) != ["laugh", "premise", "sock_voice", "twist", "update_voice"]:
            fail("drafted line is missing a craft mark")

    picked = choose(ENTRIES)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(picked, encoding="utf-8")
    OUT_PATH.chmod(0o644)

    # Read the file back and confirm it holds exactly the picked line,
    # byte for byte. A text-level comparison alone would miss a stray
    # byte-order mark or a re-encoding, so compare the raw bytes and
    # their SHA-256 digest against the picked line's encoding.
    raw = OUT_PATH.read_bytes()
    expected = picked.encode("utf-8")
    if raw != expected:
        fail("/output/entry.txt bytes do not match the picked line")
    if digest(raw) != digest(expected):
        fail("/output/entry.txt digest mismatch")
    if OUT_PATH.stat().st_size != len(expected):
        fail("/output/entry.txt has unexpected size")
    written = raw.decode("utf-8")
    problem = check_gate(written)
    if problem is not None:
        fail(f"/output/entry.txt fails gate: {problem}")
    print(picked)
    print(f"sha256: {digest(picked.encode('utf-8'))}")


if __name__ == "__main__":  # run as a script, not on import
    run()
