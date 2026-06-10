# Alibaba Cloud Deployment Adapter

This folder prepares the Alibaba Cloud proof path for the Qwen Cloud hackathon submission. It is not a claim that the service is already deployed.

## Target

- Product: Alibaba Cloud Function Compute
- Mode: custom container
- Public trigger: HTTP GET, anonymous
- App port: `8000`, matching the repository `Dockerfile`
- Runtime entry: `python -m prizepilot.webapp --host 0.0.0.0 --port 8000`

## Required Action-Time Values

Do not commit these values to the repository.

- `ALIBABA_CLOUD_ACCESS_ALIAS`: Serverless Devs access alias configured on the user's machine.
- `ALIBABA_CLOUD_REGION`: Function Compute region, for example `cn-hangzhou` or another account-supported region.
- `ACR_IMAGE`: Alibaba Cloud Container Registry image URL for the built PrizePilot image.

## Deployment Sketch

```powershell
docker build --platform linux/amd64 -t prizepilot-qwen-cloud .
docker tag prizepilot-qwen-cloud $env:ACR_IMAGE
docker push $env:ACR_IMAGE

cd deploy/alibaba-cloud
s deploy
```

## Evidence To Capture After Deployment

- Function Compute public URL.
- `/` dashboard screenshot.
- `/api/plan` JSON response.
- Link to `deploy/alibaba-cloud/s.yaml` in the public repository.
- Region, timestamp, and commit used.

## Integrity Boundary

This adapter demonstrates the intended Alibaba Cloud Function Compute configuration and the exact public code file that can be linked in Devpost. It does not complete the deployment gate until a real Alibaba Cloud account deploys the service and the public endpoint is verified.
