if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://abhishek-issac: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@github.com/Abhishek-issac/Faster.git /app
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /app
fi
cd /app
pip3 install -U -r requirements.txt
echo "starting"
python3 bot.py
