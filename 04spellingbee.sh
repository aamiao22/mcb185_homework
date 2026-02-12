gunzip -c ../MCB185/data/dictionary.gz | grep r | grep -v -E "[^acniorz]" | grep -E "^.{4,}$"

