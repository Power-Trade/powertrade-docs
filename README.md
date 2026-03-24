# Power Trade Documentation Site

This repository contains the Power Trade support documentation, migrated from GitBook to Docusaurus for cost savings and better control.

## 🚀 Local Development

```bash
# Install dependencies
npm install

# Start local dev server
npm start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## 🏗️ Build

```bash
npm run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## 📦 Deployment

The site automatically deploys to GitHub Pages when you push to the `main` branch via GitHub Actions.

### Custom Domain Setup

To use `docs.power.trade`:

1. Add a `CNAME` file to the `static` directory with `docs.power.trade`
2. Configure DNS to point `docs.power.trade` to `power-trade.github.io`
3. Enable custom domain in GitHub Pages settings

## 📝 Content Migration

This site was migrated from GitBook (`https://support.power.trade/`) to save $780/year while maintaining all functionality.

### Original Structure
- How to use PowerTrade
- Trading guides  
- Legal documentation

## 🛟 Support

- **Email**: support@power.trade
- **Telegram**: https://t.me/power_trade
- **Website**: https://power.trade

---

Built with [Docusaurus](https://docusaurus.io/) ❤️