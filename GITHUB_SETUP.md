# GitHub Setup Instructions

Your Knowbot repository is ready to be published to GitHub! Follow these steps:

## Step 1: Create a New GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository named `knowbot`
3. **Do NOT initialize with README, .gitignore, or license** (we already have these)
4. Choose visibility: Public or Private
5. Click "Create repository"

## Step 2: Connect Your Local Repository

After creating the repository on GitHub, run these commands:

```bash
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/knowbot.git

# Verify the remote was added
git remote -v

# Push your code to GitHub
git push -u origin main
```

## Step 3: Update Badge URLs

After pushing, update the badge URLs in `README.md`:

Replace `YOUR_USERNAME` in line 3 with your actual GitHub username:
```markdown
[![Python Application](https://github.com/YOUR_USERNAME/knowbot/actions/workflows/python-app.yml/badge.svg)](https://github.com/YOUR_USERNAME/knowbot/actions/workflows/python-app.yml)
```

Then commit and push:
```bash
git add README.md
git commit -m "Update: GitHub username in badges"
git push
```

## Step 4: Configure Repository Settings (Optional)

On GitHub, go to your repository settings and:

1. **Add Topics**: `python`, `rag`, `llm`, `chatbot`, `streamlit`, `weaviate`, `llamaindex`, `openai`
2. **Add Description**: "AI-powered Policy Q&A Copilot using RAG"
3. **Enable Issues**: For bug reports and feature requests
4. **Enable Discussions**: For community Q&A

## Step 5: Add Repository Secrets (for CI/CD)

If you want to run tests with actual API calls in CI/CD:

1. Go to Settings → Secrets and variables → Actions
2. Add these secrets:
   - `OPENAI_API_KEY_EMBED`
   - `WEAVIATE_URL`
   - `WEAVIATE_API_KEY`

## What's Included

Your repository now has:

✅ **README.md** - Comprehensive project documentation
✅ **QUICKSTART.md** - 5-minute setup guide
✅ **CONTRIBUTING.md** - Contribution guidelines
✅ **LICENSE** - MIT License
✅ **.gitignore** - Proper Python/IDE exclusions
✅ **.env.example** - Template for environment variables
✅ **GitHub Actions** - CI/CD workflow for testing
✅ **Badges** - Build status, license, and Python version

## Verify Everything Works

After pushing, check:

1. ✅ Repository appears on GitHub
2. ✅ README displays correctly with badges
3. ✅ GitHub Actions workflow runs (check Actions tab)
4. ✅ All files are present except `.env` (which is gitignored)

## Share Your Project

Once published, you can share:
- Repository URL: `https://github.com/YOUR_USERNAME/knowbot`
- Clone command: `git clone https://github.com/YOUR_USERNAME/knowbot.git`

## Need Help?

If you encounter issues:
- Check that your GitHub credentials are configured: `git config --global user.name` and `git config --global user.email`
- Ensure you have push access to the repository
- Verify the remote URL is correct: `git remote -v`

Happy publishing! 🚀
