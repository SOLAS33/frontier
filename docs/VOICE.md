# The Frontier voice

One voice across every site. Plain, specific, a little dry. It sounds like a well-read friend who has checked the
numbers and is not selling you anything.

## Rules

1. **Lead with the thing or the number.** "IonQ sold $2bn of new shares on 14 October." Not "Recent developments
   in the sector have seen significant capital activity."
2. **Short sentences, then one longer one.** Vary the length. Read it aloud.
3. **Say what we don't know.** "Nobody knows" beats a hedge. Mark targets as targets.
4. **Name names.** People, companies, papers, dates. Link the source.
5. **Use "we".** Never "I", never "one".
6. **Irish and British spelling.** Programme, organisation, per cent.
7. **Headlines are statements.** Each says something that could be wrong.
8. **One dry line per section, at most.** Understatement does the work. No jokes, no emoji.

## Banned

- Em dashes. Use a full stop or a comma.
- "Not X, but Y" and "it isn't about X, it's about Y".
- Three-item lists written for rhythm. List what is actually there.
- Rhetorical questions in running text.
- Colon-then-reveal sentences ("Here is the thing: ...").
- Stock words: landscape, journey, unlock, revolutionise, game-changer, cutting-edge, state-of-the-art, poised,
  robust, seamless, leverage, paradigm, testament, realm, ever-evolving, delve, dive into, tapestry, navigate,
  "in today's", "it's worth noting", "at the end of the day".
- Hype adjectives with no number behind them.

## Before and after

| Before | After |
|---|---|
| Quantum computing is poised to revolutionise industries. | Quantum computers will probably help chemistry first. Everything else is a guess. |
| It's not just a faster computer, it's a fundamentally different paradigm. | It is a different kind of machine. For most jobs it is slower. |
| The landscape is evolving rapidly. | Nine firms announced new chips this year. Two have been independently checked. |

Run `python tools/voice_lint.py` on a site before publishing. It fails the build on banned patterns.
