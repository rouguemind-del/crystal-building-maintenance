# Crystal Building Maintenance - GitHub Deployment Guide

## Quick Deploy Commands

### Step 1: Create GitHub Repository
Go to: https://github.com/new
- Repository name: `crystal-building-maintenance`  
- Public repository
- Don't initialize with anything

### Step 2: Push Local Repository
```bash
cd /Users/robbiebrady/.openclaw/workspace/crystal-building-maintenance-github
git remote add origin https://github.com/rbrady1015/crystal-building-maintenance.git
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to: https://github.com/rbrady1015/crystal-building-maintenance/settings/pages
2. Source: "Deploy from a branch"
3. Branch: main
4. Folder: / (root)
5. Save

### Step 4: View Live Website
After GitHub Pages builds (2-3 minutes):
**Live Website:** https://rbrady1015.github.io/crystal-building-maintenance/

### Step 5: Connect Custom Domain (Optional)
1. In GitHub Pages settings, add: crystalbuildingmaintenance.com
2. Update GoDaddy DNS:
   - CNAME: www → rbrady1015.github.io
   - A Records: @ → GitHub Pages IPs

## Website Will Include:
- Professional homepage with YouTube videos
- About page with 45+ year history
- Service pages (commercial, medical, condo/HOA)
- Location pages (West Palm Beach, Boca Raton)
- Advanced lead capture forms
- Mobile-responsive design
- Local SEO optimization

## Files Ready:
- 13 HTML, CSS, JS files
- Complete Git repository with commit history
- Domain configuration (CNAME file)
- Professional README documentation

**Everything is built and ready to go live!**