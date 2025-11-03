# Job Organizer - Minimal Reflex App

This is a minimal version of the Job Organizer application built with Reflex, designed to ensure proper deployment to Render before adding full functionality.

## Project Structure

```
OrgPY-Reflex2/
├── job_organizer/
│   ├── __init__.py
│   └── job_organizer.py      # Main app file
├── rxconfig.py                # Reflex configuration
├── requirements.txt           # Python dependencies
├── render.yaml               # Render deployment config
├── .gitignore
├── .env.example
└── README.md
```

## Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize Reflex:**
   ```bash
   reflex init
   ```

3. **Run the app:**
   ```bash
   reflex run
   ```

4. **Access the app:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000

## Deployment to Render

See `DEPLOYMENT_GUIDE.md` for detailed deployment instructions.

### Quick Deploy

1. Push code to GitHub
2. Connect repository to Render
3. Render will automatically detect `render.yaml`
4. Deploy!

## Testing Deployment

Once deployed, you should see:
- ✅ A page with "Job Organizer - Minimal Test" heading
- ✅ A button that responds to clicks
- ✅ Backend state updates working

If all these work, the deployment is successful and you can proceed to add the full application features.

## Next Steps

After successful deployment:
1. Add database integration (PostgreSQL)
2. Add FastAPI backend endpoints
3. Add full UI components
4. Add job management features

## Technology Stack

- **Frontend & Backend:** Reflex (Python)
- **Deployment:** Render
- **Python Version:** 3.11+
