## LLMorse - talk Morse code to LLMs! 📟🔊 🤖❓

- Multimodal LLM are bad at hearing 'CB beeps' -> ([example](https://morsecode.world/international/translator.html))
- Models seem tuned to human vocal frequency range (makes sense)
- Solution: Just record yourself saying 'beep-boop' and Morse an LLM!
- Run `python LLMorse.py` -> type your prompt (plain text) -> outputs morse-voice translation
-----
- To insert your own voice 'beep-boop':
- I recommend [Audacity](https://www.audacityteam.org/) for this, record:
- DIT (short.wav) duration: ~0.1s, DAH (long.wav) duration ~0.2s
- Adjust pitch (higher=better) if LLM struggles to distinguish short / long (as included)
- Reroute audio (loopback) using e.g. [VB-Cable](https://vb-audio.com/Cable/index.htm), mix: [Voicemeeter](https://vb-audio.com/Voicemeeter/)
- Enjoy bleeping at the AI -> hallucination-galore ensues. 🙃

---
### Excerpt from MorseLLM with GPT-4o Voice, 16/NOV/2024:

- AI: DOG: major doubledot november charlie double-duh. Gee!
- AI: -.MOM..--AND-..-POP
- AI: The word was "compute"!! \🤖/
-----
🤣👉 [Link to Video of this incident](https://youtu.be/vOCW_mK1MJs)
