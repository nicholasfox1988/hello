上传
```dos
git add .
git commit -m "any"
git push

```

…or create a new repository on the command line
```dos
echo "# java" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:nicholasfox1988/java.git
git push -u origin main
```
…or push an existing repository from the command line
```dos
git remote add origin git@github.com:nicholasfox1988/java.git
git branch -M main
git push -u origin main
```
