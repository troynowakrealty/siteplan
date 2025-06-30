#!/bin/bash
set -e

echo "🔍 Fetching latest branches from origin..."
git fetch

declare -a branches=(
  "codex/init"
  "codex/geometry-svg"
  "codex/layout"
  "codex/cli"
  "codex/tests-docs"
)

echo ""
echo "🧠 Codex Task Branch Summary:"
for branch in "${branches[@]}"; do
  echo ""
  echo "────────────────────────────────────────────"
  echo "🔄 Branch: $branch"
  git show --quiet origin/$branch --pretty="👉  %s"
  git diff --name-status origin/main..origin/$branch
done

echo ""
echo "📄 Key Files Check:"
for file in "siteplan/geometry.py" "siteplan/svg_writer.py" "siteplan/layout.py" "siteplan/cli.py" "tests/test_geometry.py" "tests/test_layout.py"; do
  echo -n "🧩 $file... "
  if git show origin/main:$file &>/dev/null || git show origin/codex/tests-docs:$file &>/dev/null; then
    echo "✅ exists"
  else
    echo "❌ missing"
  fi
done

echo ""
echo "🔗 PR Status:"
for branch in "${branches[@]}"; do
  gh pr view $branch --json title,state,headRefName --template "• {{.title}} ({{.headRefName}}): {{.state}}\n" || echo "• $branch: ❓ Not opened yet"
done

echo ""
echo "✅ All checks complete. Use 'gh pr merge <branch>' when ready to merge."
