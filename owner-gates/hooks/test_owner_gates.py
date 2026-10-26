"""Run: python3 -I hooks/test_owner_gates.py"""
import importlib.util, pathlib
spec = importlib.util.spec_from_file_location("g", pathlib.Path(__file__).with_name("owner-gates.py"))
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
asked = ["git push origin main", "git push --atomic origin main v0.3.2", "git push -f origin feat", "git push origin --tags",
         "npm publish .pack/mithaq --access public", "gh repo create me/skills --private", "npm login --auth-type=web", "gh pr merge 12"]
free = ["git push origin mithaq-upgrade", "git push origin ui-w2", "git status", "npm view some-package version", "git log main..feat"]
for c in asked: assert g.gate(c), c
for c in free: assert not g.gate(c), c
print("ok", len(asked), "gated,", len(free), "free")
