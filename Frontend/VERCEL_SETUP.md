# 🚀 Vercel Deployment Setup

## ✅ Backend Connected

Your backend is deployed at:
**https://finance-wealthprotection-production.up.railway.app**

---

## 📝 Step 1: Create Environment File

Create a `.env.local` file in the `frontend` folder:

```bash
cd frontend
```

Create `.env.local`:
```env
NEXT_PUBLIC_API_BASE=https://finance-wealthprotection-production.up.railway.app/api/v1
```

**Note**: `.env.local` is gitignored and won't be committed.

---

## 🔧 Step 2: Update Backend CORS

Your backend needs to allow requests from your Vercel frontend.

### Option A: Via Railway Dashboard (Recommended)

1. Go to [Railway Dashboard](https://railway.app)
2. Select your backend service
3. Go to **Variables** tab
4. Add new variable:
   - **Key**: `CORS_ORIGINS`
   - **Value**: `https://your-frontend.vercel.app` (you'll get this after deploying)
5. Railway will auto-redeploy

### Option B: Update Code

Edit `backend/main.py` and add your Vercel URL:

```python
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://your-frontend.vercel.app",  # Add your Vercel URL here
]
```

---

## 🚀 Step 3: Deploy to Vercel

### Via Vercel Dashboard

1. Go to [vercel.com](https://vercel.com)
2. Sign up/Login with GitHub
3. Click **"New Project"**
4. Import your repository
5. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build` (auto-detected)
   - **Output Directory**: `.next` (auto-detected)
6. **Environment Variables**:
   - Click **"Environment Variables"**
   - Add:
     - **Key**: `NEXT_PUBLIC_API_BASE`
     - **Value**: `https://finance-wealthprotection-production.up.railway.app/api/v1`
     - **Environment**: Production, Preview, Development (select all)
7. Click **"Deploy"**

### Via Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Navigate to frontend
cd frontend

# Login
vercel login

# Deploy
vercel

# Add environment variable
vercel env add NEXT_PUBLIC_API_BASE
# Enter: https://finance-wealthprotection-production.up.railway.app/api/v1
# Select: Production, Preview, Development
```

---

## ✅ Step 4: Update Backend CORS with Vercel URL

After deploying to Vercel, you'll get a URL like:
`https://your-app.vercel.app`

1. Go to Railway Dashboard → Your service → Variables
2. Update `CORS_ORIGINS` to include your Vercel URL:
   ```
   https://your-app.vercel.app
   ```
   Or if you want both local and production:
   ```
   http://localhost:3000,https://your-app.vercel.app
   ```

---

## 🧪 Step 5: Test Deployment

1. **Test Backend Health**:
   ```
   https://finance-wealthprotection-production.up.railway.app/health
   ```
   Should return: `{"status": "healthy", ...}`

2. **Test Frontend**:
   - Visit your Vercel URL
   - Try uploading a file
   - Check if dashboard loads data

3. **Check Browser Console**:
   - Open DevTools (F12)
   - Check Network tab for API calls
   - Verify requests go to Railway backend

---

## 🔍 Troubleshooting

### CORS Errors

**Error**: `Access to fetch at '...' from origin '...' has been blocked by CORS policy`

**Solution**:
1. Check Railway environment variable `CORS_ORIGINS` includes your Vercel URL
2. Ensure URL matches exactly (no trailing slash)
3. Redeploy backend after updating CORS

### API Not Found

**Error**: `Failed to fetch` or `404 Not Found`

**Solution**:
1. Verify `NEXT_PUBLIC_API_BASE` in Vercel environment variables
2. Ensure URL ends with `/api/v1`
3. Check Railway backend is running (visit health endpoint)

### Environment Variable Not Working

**Error**: Still using localhost URL

**Solution**:
1. Restart Vercel deployment
2. Clear browser cache
3. Verify variable name is exactly `NEXT_PUBLIC_API_BASE`
4. Check variable is set for all environments (Production, Preview, Development)

---

## 📋 Checklist

- [ ] Created `.env.local` with Railway backend URL
- [ ] Deployed to Vercel
- [ ] Added `NEXT_PUBLIC_API_BASE` environment variable in Vercel
- [ ] Updated Railway `CORS_ORIGINS` with Vercel URL
- [ ] Tested backend health endpoint
- [ ] Tested frontend upload functionality
- [ ] Verified API calls in browser console

---

## 🎯 Current Configuration

### API Client (`src/lib/api-client.ts`)
✅ Already configured to use `NEXT_PUBLIC_API_BASE`
✅ Falls back to `http://localhost:8000/api/v1` for local dev

### API Functions (`src/lib/api.ts`)
✅ Already configured to use `NEXT_PUBLIC_API_BASE`
✅ All endpoints use the environment variable

### Upload Function (`src/app/upload/page.tsx`)
✅ Uses `uploadFile` from `api-client.ts`
✅ Automatically uses environment variable

---

## 🔄 After Deployment

Your app will automatically:
- Use Railway backend in production
- Use localhost backend in development (if running locally)
- Handle CORS correctly
- Show real-time upload progress
- Display actual scan results

---

**Status**: ✅ Ready to deploy to Vercel!

