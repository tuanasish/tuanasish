# 🐍 Setup GitHub Contribution Snake

Để hiệu ứng "Con rắn" (Snake Animation) hoạt động trong phần GitHub Analytics, bạn cần thiết lập một GitHub Action tự động chạy hàng ngày.

## Bước 1: Tạo file Workflow
Trong repository `tuanasish` trên GitHub, tạo thư mục `.github/workflows/` (nếu chưa có) và tạo file `snake.yml` với nội dung sau:

```yaml
name: Generate Snake

on:
  schedule:
    - cron: "0 */12 * * *" # Chạy mỗi 12 tiếng
  workflow_dispatch:
  push:
    branches:
    - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Generate Snake.svg
        uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark

      - name: Push Snake.svg to the output branch
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Bước 2: Kích hoạt Action
1. Vào tab **Actions** trên repo của bạn.
2. Chọn "Generate Snake" ở cột bên trái.
3. Bấm **Run workflow**.

Sau khi chạy xong, nó sẽ tạo một branch tên là `output`. File này sẽ được README tải lên tự động!
