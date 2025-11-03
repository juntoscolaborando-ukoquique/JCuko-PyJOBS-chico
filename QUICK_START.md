# Quick Start Guide

## 🚀 Get Started in 4 Steps

### Step 1: Create Virtual Environment

```bash
cd /root/ORGANIZER-Python/PY-Reflex2-ORGANIZ/OrgPY-Reflex2

# Install venv if needed (Ubuntu/Debian)
sudo apt install python3.11-venv

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Initialize and Run

```bash
# Initialize Reflex (first time only)
reflex init

# Start the application
reflex run
```

### Step 4: Test in Browser

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

---

## 🎯 What You Should See

1. **Page loads** with "Job Organizer - Minimal Test" heading
2. **Button works** - Click "Test Backend Connection"
3. **Message updates** - Shows click count
4. **No errors** in browser console (F12)

If all these work, your setup is correct! ✅

---

## ⚠️ Important: Test Locally First!

**Always test locally before deploying to Render.** This ensures:
- Dependencies are correct
- Code has no syntax errors
- App functionality works
- You catch issues early (faster than waiting for Render builds)

---

## 📦 Deploy to Render

See `DEPLOYMENT_GUIDE.md` for complete instructions.

**Quick version:**
1. Push code to GitHub
2. Connect repo to Render
3. Render auto-detects `render.yaml`
4. Deploy!

---

## 🔧 Troubleshooting

**Reflex not found?**
```bash
pip install reflex
```

**Port already in use?**
```bash
# Kill existing process
pkill -f reflex
# Or use different port in rxconfig.py
```

**Build fails?**
```bash
# Clean and rebuild
rm -rf .web
reflex init
```

---

## 📚 Next Steps

1. ✅ Test minimal version locally
2. ✅ Deploy to Render
3. ✅ Verify deployment works
4. 📖 Follow `MIGRATION_PLAN.md` to add full features

---

## 📖 Documentation

- `README.md` - Project overview
- `DEPLOYMENT_GUIDE.md` - Complete deployment instructions
- `MIGRATION_PLAN.md` - Step-by-step migration from old project

---

**Need help?** Check the documentation or Reflex Discord: https://discord.gg/reflex
