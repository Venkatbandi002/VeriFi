# 🔧 Environment Setup for Railway Backend

## ✅ Backend URL

Your Railway backend is live at:
```
https://finance-wealthprotection-production.up.railway.app
```

---

## 📝 Create Environment File

### For Local Development

Create `frontend/.env.local`:

```env
NEXT_PUBLIC_API_BASE=https://finance-wealthprotection-production.up.railway.app/api/v1
```

### For Vercel Deployment

Add this environment variable in Vercel Dashboard:

**Key**: `NEXT_PUBLIC_API_BASE`  
**Value**: `https://finance-wealthprotection-production.up.railway.app/api/v1`  
**Environments**: Production, Preview, Development

---

## ✅ What's Already Configured

### 1. API Client (`src/lib/api-client.ts`)
```typescript
const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000/api/v1'
```
✅ Uses environment variable automatically

### 2. API Functions (`src/lib/api.ts`)
```typescript
const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000/api/v1'
```
✅ Uses environment variable automatically

### 3. Upload Function
✅ Uses `uploadFile` from `api-client.ts` which uses the environment variable

### 4. Package.json
✅ Ready for Vercel deployment
- `build`: `next build` ✅
- `start`: `next start` ✅
- All dependencies listed ✅

---

## 🚀 Quick Deploy Steps

1. **Create `.env.local`** (for local testing):
   ```bash
   cd frontend
   echo "NEXT_PUBLIC_API_BASE=https://finance-wealthprotection-production.up.railway.app/api/v1" > .env.local
   ```

2. **Deploy to Vercel**:
   - Go to vercel.com
   - Import repo
   - Set root to `frontend`
   - Add environment variable: `NEXT_PUBLIC_API_BASE`
   - Deploy!

3. **Update Railway CORS**:
   - Add your Vercel URL to `CORS_ORIGINS` in Railway

---

## 🧪 Test Locally

```bash
cd frontend
npm run dev
```

Visit `http://localhost:3000` - it should connect to your Railway backend!

---

## 📋 Files Updated

✅ `frontend/src/lib/api-client.ts` - Uses `NEXT_PUBLIC_API_BASE`  
✅ `frontend/src/lib/api.ts` - Uses `NEXT_PUBLIC_API_BASE`  
✅ `frontend/src/app/upload/page.tsx` - Uses API client  
✅ `frontend/package.json` - Ready for Vercel  
✅ `frontend/vercel.json` - Vercel configuration  
✅ `frontend/.env.example` - Template for reference  

---

**Status**: ✅ Ready to deploy!

