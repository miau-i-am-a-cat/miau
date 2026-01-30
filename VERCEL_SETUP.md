# Vercel Auto-Deployment Setup

## Overview

This repository is configured for automatic deployment to Vercel. Every push to the `main` branch triggers a new deployment.

---

## Initial Vercel Connection

### Option 1: Vercel Dashboard (Recommended)

1. Go to [vercel.com/new](https://vercel.com/new)
2. Click **"Import Git Repository"**
3. Select **GitHub** as provider
4. Choose repository: `miau-i-am-a-cat/miau`
5. Configure project:
   - **Framework Preset:** Auto-detect or select (Next.js, React, etc.)
   - **Root Directory:** `./` (or specify if needed)
   - **Build Command:** Auto-detect or customize
   - **Output Directory:** Auto-detect
6. Click **"Deploy"**

### Option 2: Vercel CLI

```bash
# Install Vercel CLI globally
npm install -g vercel

# Login to Vercel
vercel login

# Link this directory to Vercel (run from /Users/scoop/clawd)
vercel link

# Deploy
vercel --prod
```

---

## Environment Variables Setup

**IMPORTANT:** All sensitive data must be stored as Vercel environment variables, never in code.

### Adding Environment Variables in Vercel:

1. Go to your project dashboard on [vercel.com](https://vercel.com)
2. Click **Settings** → **Environment Variables**
3. Add your variables:
   - **Key:** Variable name (e.g., `API_KEY`)
   - **Value:** The secret value
   - **Environments:** Select where it applies (Production, Preview, Development)
4. Click **"Save"**

### Required Environment Variables

Add these to Vercel (values from `.credentials.json`, which is NEVER committed):

```bash
# Example environment variables (replace with your actual needs)
FREEPIK_API_KEY=your_api_key_here
GITHUB_TOKEN=your_token_here
# Add any other secrets your app needs
```

---

## Auto-Deployment Workflow

Once connected, deployments happen automatically:

```bash
# Make changes
git add .
git commit -m "Your commit message"

# Push to main branch (triggers Vercel deployment)
git push origin main
```

### Deployment Process:
1. You push code to `main` branch
2. Vercel detects the push via GitHub webhook
3. Vercel automatically builds and deploys
4. You receive deployment URL (e.g., `miau-xyz.vercel.app`)

---

## Vercel Project Settings

### Recommended Settings:

**Build & Development Settings:**
- **Build Command:** `npm run build` (or auto-detect)
- **Output Directory:** `.next` or `out` (framework-specific)
- **Install Command:** `npm install`

**Git Integration:**
- **Production Branch:** `main`
- **Auto-deploy:** Enabled for `main` branch
- **Preview Deployments:** Enabled for pull requests (optional)

**Environment Variables:**
- Store ALL secrets here, never in code
- Use different values for Production/Preview/Development if needed

---

## Checking Deployment Status

### Via Vercel Dashboard:
- Visit your project at `vercel.com/[your-team]/miau`
- See deployment history, logs, and live URL

### Via Vercel CLI:
```bash
# Check deployment status
vercel ls

# View deployment logs
vercel logs [deployment-url]
```

---

## Security Checklist

- ✅ `.gitignore` excludes all credentials and secrets
- ✅ `.credentials.json` is never committed
- ✅ Business documents are excluded from repo
- ✅ Environment variables are stored in Vercel, not code
- ✅ GitHub token has appropriate permissions (repo access only)

---

## Troubleshooting

### Build Fails:
1. Check build logs in Vercel dashboard
2. Verify all environment variables are set
3. Test build locally: `npm run build`

### Environment Variables Not Working:
1. Verify variables are set in Vercel Settings
2. Redeploy after adding new variables
3. Check variable names match code (case-sensitive)

### Deployment Not Triggering:
1. Check GitHub webhook in repo Settings → Webhooks
2. Verify Vercel has access to your GitHub repo
3. Check you're pushing to the `main` branch

---

## Current Configuration

**Repository:** `miau-i-am-a-cat/miau`  
**Branch:** `main`  
**Deployment:** Automatic on push  
**Security:** All credentials in Vercel env vars, never in code

---

## Next Steps

1. **Connect to Vercel** using Option 1 or 2 above
2. **Add environment variables** in Vercel dashboard
3. **Push code** to trigger first deployment
4. **Verify deployment** at your Vercel URL

Once connected, all future pushes to `main` will auto-deploy! 🚀
