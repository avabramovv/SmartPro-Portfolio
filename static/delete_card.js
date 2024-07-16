function deleteCard(projectId) {
    // Найти карточку по ID проекта
    var card = document.querySelector(`.fair-card[data-project-id="${projectId}"]`);
    if (card) {
        // Удалить карточку из DOM
        card.remove();
    }

    // Отправить запрос на сервер для удаления проекта из базы данных
    fetch(`/delete_project/${projectId}`, {
        method: 'DELETE'
    }).then(response => {
        if (response.ok) {
            console.log('Проект успешно удален');
        } else {
            console.error('Ошибка при удалении проекта');
        }
    }).catch(error => {
        console.error('Ошибка при удалении проекта:', error);
    });

    // history.replaceState(null, null, document.URL);

    // window.location.href = '/';
}