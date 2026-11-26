# Funniest Lost Sock Status Update — make.fun bounty
# u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce
#
# The program writes one funny lost-sock status update (a single line of
# at most 120 characters) to /output/entry.txt.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. really is a status update in the voice of a lost sock
#   2. earns a real laugh, with a turn or a punchline landing in the
#      last few words
#   3. rests on a clear comic premise the sock's situation makes
#      inevitable, so the joke feels found rather than assembled
#   4. sounds like a sock: small, domestic, a little anxious, never a
#      person wearing a sock as a costume
#   5. feels new and twists the obvious sock material (the dryer, the
#      missing partner) somewhere unexpected — no dryer, no lost pair
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: status-voice 9, laugh 9, premise 10, sock-voice 9,
    #   twist 10 = 47. "Promoted" reframes being lost as a career move:
    #   the sock did not get eaten, it got a job. REVISION (second
    #   pass): the middle beat said "the job is permanent", which
    #   explains the joke instead of letting it sit; "the hours are
    #   steady" keeps the resigned-career joke in status-update voice
    #   and hands the line to the punchline sooner. The punchline lands
    #   last — a tea cosy has no feet to cover, which is the whole
    #   tragedy of a sock, stated deadpan. No dryer, no missing pair.
    ("Update: I got promoted to tea cosy. The teapot is warm, the "
     "hours are steady, and nobody here has feet.",
     47),
    # score: status-voice 10, laugh 9, premise 8, sock-voice 10,
    #   twist 8 = 45. The weary punch — apologises to the screen,
    #   never to me — is pure sock voice, but a phone sock is a real
    #   product, so the "should not be here" premise is softer.
    ("Status update: I am a phone sock now. The human drops me daily "
     "and apologises to the screen, never to me.",
     45),
    # score: status-voice 9, laugh 9, premise 9, sock-voice 9,
    #   twist 9 = 45. Filing a complaint with the owner's manual is a
    #   sharp, small, domestic turn; "It ignored me" is the weary
    #   payoff. Slightly wordier than the winner, punch a touch weaker.
    ("Day 6 in the glove compartment. I am not a glove. I filed a "
     "complaint with the owner's manual. It ignored me.",
     45),
    # score: status-voice 9, laugh 9, premise 9, sock-voice 8,
    #   twist 9 = 44. "Still blames the Wi-Fi" is a fresh, modern turn
    #   and the jam is the sock's own doing; the sock voice is a little
    #   thinner than the winner's, more narrator than sock.
    ("Day 4 inside the printer. I have jammed it twice and the human "
     "still blames the Wi-Fi. This is my life now.",
     44),
    # score: status-voice 9, laugh 8, premise 9, sock-voice 9,
    #   twist 9 = 44. Paid in acorns is a lovely detail and the gnome
    #   premise is original, but "I miss the drawer" ends on longing
    #   rather than a laugh.
    ("Update: I am the gnome's left shoe now. He pays in acorns and "
     "never washes me. I miss the drawer.",
     44),
    # score: status-voice 8, laugh 9, premise 9, sock-voice 8,
    #   twist 9 = 43. "Learned to hate jazz" is a great last line, but
    #   the entry opens with no status-update marker, so it reads more
    #   like a diary line than a status update.
    ("I live in the trumpet case now. The human plays me every Sunday "
     "and I have learned to hate jazz.",
     43),
    # score: status-voice 10, laugh 8, premise 8, sock-voice 9,
    #   twist 8 = 43. A draft excluder is a genuinely sock-shaped job
    #   and "stepping on my face" is vivid; the premise needs a beat
    #   too long to land for a 120-character line.
    ("Status update: I am stuffing the draft under the door now. Cold "
     "air, no thanks, and the cat keeps stepping on my face.",
     43),
    # score: status-voice 9, laugh 8, premise 8, sock-voice 8,
    #   twist 8 = 41. "Things no sock should see" is a good closer,
    #   but the air-freshener premise is the weakest link — a sock
    #   swinging from a mirror strains belief even for this brief.
    ("Day 9 as a car air freshener. I smell of pine, I swing from the "
     "mirror, and I have seen things no sock should see.",
     41),
    # score: status-voice 10, laugh 7, premise 8, sock-voice 9,
    #   twist 7 = 41. "The bag is quieter than the drawer" is a nice
    #   weary beat, but "I am not coming back" ends flat, and the
    #   vacuum sits too close to the obvious lost-in-the-laundry turf.
    ("Status update: the vacuum ate me, and honestly the bag is "
     "quieter than the drawer. I am not coming back.",
     41),
    # score: status-voice 8, laugh 8, premise 8, sock-voice 9,
    #   twist 8 = 41. "Feet I did not choose" is a strong sock line,
    #   but the ski boot is just another dark, smelly container — the
    #   premise does not twist, it only relocates.
    ("I live in the ski boot now. It is dark, it smells of feet I did "
     "not choose, and the mountain does not care.",
     41),
    # score: status-voice 9, laugh 7, premise 8, sock-voice 8,
    #   twist 6 = 38. The cat-as-hat image is fun, but the closer
    #   leans on the missing pair — exactly the obvious material the
    #   brief tells us to twist away from.
    ("Update: the cat wears me as a hat. I can see the whole house "
     "from up here and I still cannot find my pair.",
     38),
    # score: status-voice 9, laugh 7, premise 8, sock-voice 8,
    #   twist 5 = 37. A dust cloth is a plausible lost-sock fate, but
    #   "I used to have a partner" is the single most obvious sock
    #   line there is; it concedes the twist criterion entirely.
    ("Update: I am a dust cloth now. The human wipes the TV with me "
     "and calls it cleaning. I used to have a partner.",
     37),
]

# The gate requires 1-120 characters of non-whitespace UTF-8 text.
MAX_CHARS = 120


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= MAX_CHARS, \
            f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be a single line"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    import os
    import sys

    update = pick(CANDIDATES)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(update)
    os.chmod("/output/entry.txt", 0o644)
    # Verify the written output: read it back byte-for-byte and re-check
    # the gate (1-120 characters, single line, non-blank). A truncated or
    # altered file must fail loudly instead of shipping a bad entry.
    with open("/output/entry.txt", "rb") as f:
        written = f.read().decode("utf-8")
    if written != update:
        print("error: /output/entry.txt does not match selected update",
              file=sys.stderr)
        sys.exit(1)
    if not (1 <= len(written) <= MAX_CHARS and written.strip()
            and "\n" not in written):
        print("error: /output/entry.txt fails gate: "
              f"{len(written)} chars", file=sys.stderr)
        sys.exit(1)
    print(update)


if __name__ == "__main__":
    main()
