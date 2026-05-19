```bash
git filter-repo --commit-callback '
if commit.author_email == b"old@example.com":
    commit.author_name = b"lumynous"
    commit.author_email = b"new@example.com"
'
```


```bash
git filter-repo --commit-callback '
if commit.committer_email == b"limingyan@tdh.com":
    commit.committer_name = b"limingyan320"
    commit.committer_email = b"1290229040@qq.com"
'
```
