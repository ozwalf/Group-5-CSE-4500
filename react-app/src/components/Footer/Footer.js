import './Footer.css'
import { FooterData } from './FooterData'
import github_logo from '../../images/github-mark.png'

function Footer() {

    return (
        <div className="footer">
            <ul className='footer-item'>
            {FooterData.map((item, index) => {
                return (
                    <li key={index}>
                        <a href={item.path} target='_blank' rel="noreferrer">
                        <img className={item.cName} src={github_logo} alt={item.alt}/>
                        </a>
                    </li>
                );
            })}
            </ul>
      </div>

  
    )
}

export default Footer