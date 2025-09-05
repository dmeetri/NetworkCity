import { Link } from "react-router-dom";

import "./header.css";

const currentDate = new Date();
const formattedDate = currentDate.toLocaleString('ru-RU', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    weekday: 'long',
});

export const Header = () => {
    return (
        <header className="header">
            <div className="top-header">
                <div className="container">
                    <div className="top-header-content flex">
                        <div className="header-organization-info">
                            <h2 className="pt-sans-bold">NETWOR-CITY ЧТОТиБ</h2>
                        </div>

                        <div className="header-base-info">
                            <div className="teacher-info">
                                ФИО учителя
                            </div>

                            <div className="date-info">
                                <p>
                                    {formattedDate} | Работают: 5
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="bottom-header">
                <div className="container">
                    <nav>
                        <Link className="header-bottom-link" to="/">Группы</Link>
                        <Link className="header-bottom-link" to="/">Студенты</Link>
                        <Link className="header-bottom-link" to="/">Предметы</Link>
                        <Link className="header-bottom-link" to="/">Расписание</Link>
                        <Link className="header-bottom-link" to="/">Журнал</Link>
                    </nav>
                </div>
            </div>
        </header>
    );
}