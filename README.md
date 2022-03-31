gh-mirror is a simple way to mirror a user's GitHub repositories locally,
maintaining the upstream repository metadata, and keep them updated easily. See
[the blog post I wrote it for][blog] to get more information about how to use
it in a useful way.

```
$ gh-mirror cdown
Cloning into bare repository 'Apache-ETag.git'...
remote: Counting objects: 7, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 7 (delta 0), reused 6 (delta 0)
Receiving objects: 100% (7/7), done.
Checking connectivity... done.
Cloning into bare repository 'bats.git'...
[...]
```

[blog]: https://chrisdown.name/2013/07/05/setting-up-local-github-mirror-with-cgit-git-daemon.html

## License

gh-mirror is [ISC licensed][isc]. See the LICENSE file for full details.

[isc]: http://en.wikipedia.org/wiki/ISC_license
