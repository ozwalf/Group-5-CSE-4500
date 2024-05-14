import React from 'react';

const Tags = ({ repeatCount }) => {

        const tags = [
        'div', 'a', 'input', 'span', 'p', 'button', 
        'form', 'label', 'section', 'article', 'header', 
        'footer', 'nav', 'aside', 'h1', 'h2', 'h3', 'h4', 
        'h5', 'h6', 'ul', 'ol', 'li', 'table', 'thead', 
        'tbody', 'tr', 'td', 'th', 'blockquote', 'pre', 
        'code', 'iframe', 'img', 'video', 'audio', 'canvas', 
        'svg', 'figure', 'figcaption', 'details', 'summary'
    ];

    const generateTags = (repeatCount) => {
            const repeatedTags = [];
            for (let i = 0; i < repeatCount; i++) {
                tags.forEach((Tag, index) => {
                    repeatedTags.push(<Tag key={`${Tag}-${i}-${index}`} />);
                });
            }
            return repeatedTags;
    };

    return (
            <div style={{ display: 'none' }}>
                {generateTags(repeatCount)}
            </div>
    );
};

export default Tags;
