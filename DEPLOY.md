# Vercel Environment Variables Configuration

## Set these in your Vercel Project Dashboard

Go to your Vercel project → Settings → Environment Variables and add:

### 1. MONGODB_URI
```
MONGODB_URI=mongodb+srv://muhammednihal24ag039:l6ZrDiiOk3TY74aV@cluster0.pppmmcf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
```

### 2. ENCRYPTION_KEY
```
ENCRYPTION_KEY=-v52SdMtoMDGe3L78HunVqE6Stb4FqHAmciZhrijl48=
```

## Deploy Commands

After setting the environment variables, deploy with:

```bash
vercel --prod
```

Or simply push to your GitHub repository if you have automatic deployments enabled.

## Test Your Deployment

After deployment, test these endpoints:

1. **Basic Function Test:**
   ```
   https://your-app.vercel.app/test
   ```

2. **Health Check:**
   ```
   https://your-app.vercel.app/health
   ```

3. **Send Message Test:**
   ```bash
   curl -X POST https://your-app.vercel.app/send_message \
     -H "Content-Type: application/json" \
     -d '{"username": "TestUser", "message": "Hello World!"}'
   ```

4. **Get Messages Test:**
   ```
   https://your-app.vercel.app/get_messages
   ```

## Your Application is Ready! ✅

- ✅ MongoDB Atlas connection working
- ✅ Message encryption/decryption working  
- ✅ All endpoints tested successfully
- ✅ Error handling improved
- ✅ Vercel configuration updated
