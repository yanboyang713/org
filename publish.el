;; https://github.com/jethrokuan/braindump/blob/master/publish.el
(require 'find-lisp)
(require 'ox-hugo)

;;(projectile-mode -1)
;;(dtrt-indent-mode -1)
(recentf-mode -1)


(defun boyang/publish (file)
  "Publish a note in FILE."
  (with-current-buffer (find-file-noselect file)
    (setq org-hugo-section "notes"
          org-hugo-base-dir "~/personalblog/")
    ;;(let ((org-id-extra-files (find-lisp-find-files org-roam-directory "\.org$")))
    (let ((org-id-extra-files (find-lisp-find-files "/home/yanboyang713/org/references/notes" "\.org$")))
      (org-hugo-export-wim-to-md))))
