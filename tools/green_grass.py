import os
import random
from datetime import datetime, timedelta

# --- CONFIGURATION ---
REPO_PATH = os.path.dirname(os.path.abspath(__file__)) # Thư mục hiện tại (profile readme)
CONTRIBUTION_FILE = os.path.join(REPO_PATH, "CONTRIBUTION.md")
COMMIT_MESSAGE = "chore: daily contribution [auto]"
GIT_USER_NAME = "tuanasish"
GIT_USER_EMAIL = "vuanhtuanofc@gmail.com"

def run_command(command):
    print(f"Executing: {command}")
    os.system(command)

def setup_git_identity():
    run_command(f'git config user.name "{GIT_USER_NAME}"')
    run_command(f'git config user.email "{GIT_USER_EMAIL}"')

def make_grass_green(days=30, commits_per_day_range=(1, 5)):
    """
    Tự động tạo commit trong quá khứ để làm xanh biểu đồ.
    """
    setup_git_identity()
    print(f"🚀 Bắt đầu chiến dịch 'Xanh Cỏ' trong {days} ngày...")
    
    # Đảm bảo file tồn tại
    if not os.path.exists(CONTRIBUTION_FILE):
        with open(CONTRIBUTION_FILE, "w") as f:
            f.write("# GitHub Contribution History\n")

    current_date = datetime.now()

    for i in range(days):
        # Lùi ngày về phía sau
        target_date = current_date - timedelta(days=i)
        
        # Số lượng commit ngẫu nhiên mỗi ngày
        num_commits = random.randint(*commits_per_day_range)
        
        for j in range(num_commits):
            # Tạo thay đổi trong file
            with open(CONTRIBUTION_FILE, "a") as f:
                f.write(f"- Contribution on {target_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            # Format ngày cho git
            # Windows powershell/cmd format
            date_str = target_date.strftime("%Y-%m-%dT%H:%M:%S")
            
            # Thực hiện commit với ngày giả lập
            os.environ['GIT_AUTHOR_DATE'] = date_str
            os.environ['GIT_COMMITTER_DATE'] = date_str
            
            run_command(f'git add "{CONTRIBUTION_FILE}"')
            run_command(f'git commit -m "{COMMIT_MESSAGE}" --date="{date_str}"')

    print("\n✅ Đã tạo xong các commit cục bộ.")
    print("💡 Tiếp theo: Anh hãy chạy lệnh 'git push origin main' để đẩy lên GitHub.")

if __name__ == "__main__":
    # Mặc định tạo 30 ngày gần nhất
    make_grass_green(days=30)
