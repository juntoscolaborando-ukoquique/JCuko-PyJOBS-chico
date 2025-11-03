# Render Deployment - Step by Step

## How Render Handles Port Management

### Port Conflicts Cannot Happen

**Important:** You don't need to worry about port conflicts. Here's why:

1. **Container Isolation:** Each deployment runs in its own isolated container (like a separate virtual machine)
2. **Separate Network Namespaces:** Port 10000 in Container A is completely separate from port 10000 in Container B
3. **Automatic Port Assignment:** Render assigns a free port from its pool and sets the `PORT` environment variable
4. **Zero-Downtime Deployments:** Old container keeps running until new container passes health checks, then old is killed

**Analogy:** Like apartment buildings - Building A Apartment 10000 and Building B Apartment 10000 don't conflict because they're in different buildings.

**What Render Does:**
```
1. Creates new container with fresh environment
2. Assigns free PORT (e.g., 10000, 10001, etc.)
3. Your app reads PORT and binds to 0.0.0.0:$PORT
4. Render detects open port and routes traffic
5. Old container is killed after traffic switches
```

**Your Only Responsibility:**
- ✅ Read `PORT` from environment variable
- ✅ Bind to `0.0.0.0:$PORT` (all interfaces)
- ✅ Respond to health checks

---

## Solution: Connect GitHub to Render

### Step 1: Go to Render Dashboard
- Visit: https://dashboard.render.com

### Step 2: Connect GitHub Account
1. Click on your **profile icon** (top right corner)
2. Select **"Account Settings"**
3. Scroll down to **"Connected Services"** or **"GitHub"**
4. Click **"Connect GitHub"** or **"Authorize"**
5. You'll be redirected to GitHub
6. Click **"Authorize render"** to allow Render to access your repositories

### Step 3: Grant Repository Access
1. After authorizing, you may need to select which repositories Render can access
2. Select **"JCuko-PyJOBS-chico"** repository
3. Click **"Install"** or **"Approve"**

### Step 4: Return to Render and Create Blueprint
1. Go back to: https://dashboard.render.com
2. Click **"New +"** button (top right)
3. Select **"Blueprint"**
4. Now you should see your GitHub repositories listed
5. Select **"JCuko-PyJOBS-chico"**
6. Render will auto-detect `render.yaml`

### Step 5: Review and Deploy
1. Review the configuration
2. Click **"Apply"**
3. Build will start automatically

---

## Alternative: Manual Web Service (If Blueprint Doesn't Work)

If Blueprint still has issues:

1. Go to: https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Click **"Build and deploy from a Git repository"**
4. Paste: `https://github.com/juntoscolaborando-ukoquique/JCuko-PyJOBS-chico`
5. Click **"Next"**
6. Configure:
   - **Name:** `job-organizer-minimal`
   - **Branch:** `master`
   - **Build Command:** `pip install -r requirements.txt && reflex init`
   - **Start Command:** `reflex run --env prod`
   - **Plan:** Free
7. Click **"Create Web Service"**

---

## Troubleshooting

### "No repositories found"
- GitHub not connected
- Solution: Follow Step 2 above (Connect GitHub)

### "Repository not showing"
- Render doesn't have access to that repo
- Solution: Go to GitHub → Settings → Applications → Render → Grant access to "JCuko-PyJOBS-chico"

### "Can't find render.yaml"
- File not pushed to GitHub
- Solution: Verify at: https://github.com/juntoscolaborando-ukoquique/JCuko-PyJOBS-chico
- All files should be visible there

---

## Verify GitHub Push

Check that all files are on GitHub:
https://github.com/juntoscolaborando-ukoquique/JCuko-PyJOBS-chico

You should see:
- ✅ `render.yaml`
- ✅ `requirements.txt`
- ✅ `rxconfig.py`
- ✅ `job_organizer/` folder
- ✅ All documentation files

---

## Next Steps

1. **Connect GitHub to Render** (if not done)
2. **Create Blueprint** with auto-detected `render.yaml`
3. **Deploy** and wait for build
4. **Verify** at the provided URL

Let me know which step you're stuck on!
