import os
import pygit2
from github import Github


class GitController(object):
    def create_repo(self, prefs, project_name):
        g = Github(prefs['credentials']['username'],
                   prefs['credentials']['password'])
        user = g.get_user()

        repo = None
        try:
            repo = user.create_repo(project_name)
            repo.create_file("README.md", "init commit", "initial commit")
        except Exception:
            repo = user.get_repo(project_name)

        repoClone = pygit2.clone_repository(
            repo.git_url, os.path.join(prefs['localRepo'], project_name))

        repoClone.remotes.set_url("origin", repo.clone_url)
        index = repoClone.index
        index.add_all()
        index.write()

        author = pygit2.Signature(user.name, user.email)
        commiter = pygit2.Signature(user.name, user.email)

        tree = index.write_tree()
        oid = repoClone.create_commit('refs/heads/master', author, commiter,
                                      "init commit", tree, [repoClone.head.target.hex])
        print(oid)
        remote = repoClone.remotes["origin"]
        credentials = pygit2.UserPass(
            prefs['credentials']['username'], prefs['credentials']['password'])
        remote.credentials = credentials

        callbacks = pygit2.RemoteCallbacks(credentials=credentials)

        remote.push(['refs/heads/master'], callbacks=callbacks)


if __name__ == "__main__":
    git = GitController()
    prefs = {}
    prefs['localRepo'] = "E:/repository/python/test"
    prefs['credentials'] = {}
    prefs['credentials']['username'] = 'yourusername'
    prefs['credentials']['password'] = 'yourpassword'
    git.create_repo(prefs, 'new_project3333')
