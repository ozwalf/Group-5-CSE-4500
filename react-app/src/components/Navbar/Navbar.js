import './Navbar.css'
import { NavbarData } from './NavbarData'


function Navbar() {

    return (
        <nav className="navbar">
            <h1 className="nav-title">
                <a href='/'>
                    Platform Computing
                </a>
            </h1>
            <ul className='page-item'>
            {NavbarData.map((item, index) => {
                return (
                    <li key={index}>
                        <a href={item.path} className={item.cName}>
                        {item.title}
                        </a>
                    </li>
                );
            })}
            </ul>
      </nav>
    )
}

export default Navbar