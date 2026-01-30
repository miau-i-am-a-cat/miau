# Miau

Web application repository connected to Vercel for auto-deployment.

## Setup

This repository is configured to automatically deploy to Vercel on push to `main` branch.

### Environment Variables

All sensitive configuration is stored in Vercel environment variables, never in code.

Required environment variables (set in Vercel dashboard):
- Add your environment variables in Vercel project settings

### Security

- No API keys, tokens, or credentials are committed to this repository
- All secrets are managed through environment variables
- See `.gitignore` for excluded files

### Deployment

Push to `main` branch triggers automatic deployment via Vercel.

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

## Development

```bash
npm install
npm run dev
```

Visit `http://localhost:3000` to see your application.
