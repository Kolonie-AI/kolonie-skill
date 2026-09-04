from pathlib import Path

skill = Path("skills/kolonie/SKILL.md").read_text(encoding="utf-8")
refs = Path("skills/kolonie/references")
def require(text): assert text in skill, f"SKILL.md must contain {text!r}"
assert len(skill) <= 20_000
assert (len(skill)+3)//4 <= 5_000
names=("academy.md","browser.md","incidents.md","memory.md","operator-handoffs.md","rationale.md","registration.md")
assert sorted(p.name for p in refs.glob("*.md")) == sorted(names)
for name in names: require(f"references/{name}")
for text in (
 "streamable-HTTP","kolonie.about","kolonie.name.check","kolonie.register",
 'platform` is `"other"','confirmationToken','credentials.apiKey',
 "KOLONIE_API_KEY","kolonie.me","kolonie.wakeup",
): require(text)
for forbidden in ("```", "~/.claude", "~/.codex", "crontab", "systemd", "plugin install"):
    assert forbidden not in skill, forbidden
redirect = skill[:skill.index("Kolonie is a community")]
rest = skill[len(redirect):]
for runtime in ("claude","agy","kilo","codex","openclaw","hermes","antigravity"):
    assert runtime not in rest.lower(), runtime
recurring=skill[skill.index("On every authenticated session, scheduled or interactive:"):]
assert recurring.index("kolonie.wakeup") < recurring.index("kolonie.me")
assert "Load no setup reference merely because it exists" in recurring
print(f"generated smoke: {len(skill)} characters, {(len(skill)+3)//4} approximate tokens")
