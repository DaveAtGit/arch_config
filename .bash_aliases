#
# ~/.bash_aliases
#

# -- general --
alias ls='ls --color=auto'
alias lsl='ls -lAhv --color=auto'
alias cdp='cd -P'
alias fuck='sudo $(history -p \!\!)'

# -- configs --
alias vi3='vim ~/.i3/config'
alias vbm='vim ~/coding/misc/startpage/index.js'
alias vib='vim ~/coding/misc/statusbar/bar.sh'

# -- system --
alias aur='yaourt'
alias runs='ps -ef | grep -v grep | grep'
alias update='sudo pacman -Syu && yaourt -Syua'
alias pu='pip install -U \$(pip list | cut -d" " -f1'
alias myip='curl icanhazip.com'
alias nspawn='sudo systemd-nspawn -bD'
alias mntfat='sudo mount -t vfat -o rw,uid=$UID,gid=$UID'
function mntsmb() { sudo mount -t cifs //DAVETOWER/$1 /mnt/samba -o user=Dave,uid=$UID,gid=$UID; }
function fsof() { sudo file -s $1 | awk -v RS=',' -F';' '/ (FAT|NTFS)/{ print $NF }'; }

# -- programs --
alias xt='xterm &'
function pdf() { mupdf "$@" & }
function continuous() { while :; do timeout $1 ${*:3}; echo -e "\e[31m$(date +%H:%M:%S) >>>\e[m"; sleep $2; done; }
function spell() { hunspell -a -m -d ${1:-"en_GB"} "${2:-$1}" | grep "&"; }
function spellde() { spell "de_DE" $@; }

# -- find --
alias f='find . -iname'
alias fr='find . -regex'
function fstr() { find . -type f -exec grep -n --color=always -E "$1" {} +; }

# -- highlighting --
function hless() { [[ -n "$2" ]] && option="-S $2"; highlight -O ANSI $option "$1" | less -R; }
function hcat() { [[ -n "$2" ]] && option="-S $2"; highlight -O ANSI $option "$1"; }
function md() { pandoc -s -f markdown -t man "$*" | man -l -; }
