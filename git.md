puДобавить или изменить имя пользователя
git config --global user.name x

Добавить или изменить электронную почту
git config --global user.email x@mail.ru

Получить информацию о текущих настройках
git config --list

Узнать конкретную настройку
git config user.name

Получить информацию о функциях
git --help

Сохранить удаленный репозиторий на локальной машине 
git clone git@github.com:x_name/x_repo.git

Создать локальный репозиторий
git init

Создать файл README
touch README

Внести файл во временное хранилище (индексировать)
git add README

Внести все файлы
git add .

Удалить индексацию файла
git rm -cashed README

Удалить файл из индекса и проекта
git rm -f README

Определить состояние файлов
git status

Перенести файл в локальный репозиторий (сделать коммит)
git commit -m "success"

Посмотреть историю коммитов
git log

Связать локальный репозиторий с GitHub
git remote add origin git@ithub.com:name/repo.git

Проверить связался ли локальный репозиторий с удаленным
git remote get-url origin

Удалить связь лоального и удаленного репозитория
git remote remove origin

Отправить изменения в удаленный репозиторий origin ветки master
git push origin master

Отправить изменения с текущей ветки репозитория
git push

Проверить внесенные изменения
git pull



