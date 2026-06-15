# Demo Video URL Candidates

Status: local WebM generation ready; Devpost rejected GitHub-hosted WebM as the required video demo link.

## Local Asset

- `docs/demo-video/prizepilot-demo.webm`

## Public URL Candidates After GitHub Push

- GitHub file page: `https://github.com/OOYXLOO/prizepilot-qwen-cloud/blob/main/docs/demo-video/prizepilot-demo.webm`
- Raw file URL: `https://raw.githubusercontent.com/OOYXLOO/prizepilot-qwen-cloud/main/docs/demo-video/prizepilot-demo.webm`

Devpost result: rejected for the required Qwen Project details video field with `must be a valid YouTube, Facebook Video, Vimeo or Youku URL`.

Qwen official requirement observed on the Devpost overview page: the demo video should be uploaded to YouTube, Vimeo, or Facebook Video and made public. Treat Youku as a Devpost field-level fallback only if organizers explicitly accept it for this Qwen event.

## Supported Host Needed

Upload `docs/demo-video/prizepilot-demo.webm` to one of:

- YouTube
- Facebook Video
- Vimeo

## Current Host Check

- YouTube upload check on 2026-06-10: `https://www.youtube.com/upload` opened a Google sign-in page, so no usable YouTube upload session is currently available in the browser.
- YouTube official upload flow starts with signing in to YouTube Studio: https://support.google.com/youtube/answer/57407
- Vimeo official upload flow uses the user's Vimeo upload page/library: https://help.vimeo.com/hc/en-us/articles/18774922216721-How-to-upload-a-video-to-Vimeo
- Do not reuse unrelated credentials for a video platform account. If an authenticated YouTube, Vimeo, or Facebook Video session becomes available, upload the local WebM, make it publicly accessible, and record the accepted URL in `docs/qwen-route-ledger.md`.

## Notes

- The WebM is silent and rendered only from public local demo assets.
- After upload, record the accepted URL in `docs/qwen-route-ledger.md`, then return to the Qwen Devpost Project details page.
