# Troubleshooting Guide for FUNCTION_INVOCATION_FAILED

## What I Fixed:

### 1. **Vercel Configuration Issues**
- Updated `vercel.json` to properly point to `vercel.py` instead of `app.py`
- Simplified the routing configuration

### 2. **Environment Variables**
- Added proper error handling for missing `MONGODB_URI`
- Added proper error handling for missing `ENCRYPTION_KEY`
- Created `.env.example` with templates

### 3. **MongoDB Connection Issues**
- Fixed the `server_api` parameter to only be used with MongoDB Atlas
- Added better error handling that doesn't crash the app
- Added database availability checks in endpoints

### 4. **Added Better Error Handling**
- Added service availability checks
- Added comprehensive error responses
- Added a test endpoint `/test` for debugging

## Steps to Deploy Successfully:

### 1. **Set Environment Variables in Vercel:**
Go to your Vercel project dashboard → Settings → Environment Variables and add:

```
MONGODB_URI=your_mongodb_atlas_connection_string
ENCRYPTION_KEY=-v52SdMtoMDGe3L78HunVqE6Stb4FqHAmciZhrijl48=
```

### 2. **MongoDB Setup:**
- If using MongoDB Atlas, make sure your connection string is correct
- Ensure your IP address is whitelisted in MongoDB Atlas
- Test the connection string locally first

### 3. **Test Endpoints:**
After deployment, test these endpoints:
- `/test` - Basic function test
- `/health` - Database health check
- `/` - Main application

### 4. **Check Logs:**
- Visit your Vercel project → Functions → View Logs
- Or visit `https://your-app.vercel.app/_logs`

## Common Issues and Solutions:

### Issue: Database Connection Failed
**Solution:** Check if MONGODB_URI is set correctly and accessible

### Issue: Encryption Errors
**Solution:** Ensure ENCRYPTION_KEY is set and valid

### Issue: Import Errors
**Solution:** Check if all dependencies in requirements.txt are available

### Issue: Route Not Found
**Solution:** Verify vercel.json configuration is correct

## Testing Commands:

```bash
# Test locally
python app.py

# Test specific endpoints
curl http://localhost:5000/test
curl http://localhost:5000/health

# Generate new encryption key
python generate_key.py
```

## Next Steps:

1. Set the environment variables in Vercel
2. Redeploy your application
3. Test the `/test` endpoint first
4. Check `/health` endpoint for database status
5. If issues persist, check the Vercel function logs
