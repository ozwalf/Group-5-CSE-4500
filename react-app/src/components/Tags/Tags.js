import React from 'react';
import './Tags.css'

const Tags = ({ repeatCount }) => {
  // tag components with info content
  const tags = [
    { tag: 'div', content: 'This is a div' },
    { tag: (props) => <a href="/" target="_blank" rel="noreferrer" {...props}>This is a link</a>, content: '' },
    { tag: 'input', content: null },
    { tag: 'span', content: 'This is a span' },
    { tag: 'p', content: 'This is a paragraph' },
    { tag: 'button', content: 'This is a button' },
    { tag: 'form', content: 'This is a form' },
    { tag: 'label', content: 'This is a label' },
    { tag: 'section', content: 'This is a section' },
    { tag: 'article', content: 'This is an article' },
    { tag: 'header', content: 'This is a header' },
    { tag: 'footer', content: 'This is a footer' },
    { tag: 'nav', content: 'This is a nav' },
    { tag: 'aside', content: 'This is an aside' },
    { tag: 'h1', content: 'This is an h1' },
    { tag: 'h2', content: 'This is an h2' },
    { tag: 'h3', content: 'This is an h3' },
    { tag: 'h4', content: 'This is an h4' },
    { tag: 'h5', content: 'This is an h5' },
    { tag: 'h6', content: 'This is an h6' },
    { tag: 'ul', content: <li>This is a list item</li> },
    { tag: 'ol', content: <li>This is an ordered list item</li> },
    { tag: 'li', content: 'This is a list item' },
    { tag: 'table', content: <tr><td>This is a table cell</td></tr> },
    { tag: 'thead', content: <tr><th>This is a table header</th></tr> },
    { tag: 'tbody', content: <tr><td>This is a table body cell</td></tr> },
    { tag: 'tr', content: <td>This is a table row</td> },
    { tag: 'td', content: 'This is a table data' },
    { tag: 'th', content: 'This is a table header' },
    { tag: 'blockquote', content: 'This is a blockquote' },
    { tag: 'pre', content: 'This is preformatted text' },
    { tag: 'code', content: 'This is a code block' },
    { tag: 'iframe', content: 'This is an iframe' },
    { tag: 'img', content: null },
    { tag: 'video', content: 'This is a video' },
    { tag: 'audio', content: 'This is an audio' },
    { tag: 'canvas', content: 'This is a canvas' },
    { tag: 'svg', content: 'This is an svg' },
    { tag: 'figure', content: 'This is a figure' },
    { tag: 'figcaption', content: 'This is a figcaption' },
    { tag: 'details', content: 'This is a details' },
    { tag: 'summary', content: 'This is a summary' }
  ];

  const generateRepeatedTags = (repeatCount) => {
    const repeatedTags = [];
    for (let i = 0; i < repeatCount; i++) {
      tags.forEach(({ tag: Tag, content }, index) => {
        if (typeof Tag === 'string') {
          repeatedTags.push(React.createElement(Tag, { key: `${Tag}-${i}-${index}` }, content));
        } else {
          repeatedTags.push(<Tag key={`a-${i}-${index}`} />);
        }
      });
    }
    return repeatedTags;
  };

  return (
    <div className='tags'>
        <h1>Below is a list of the most popular HTML tags used today</h1>
        {generateRepeatedTags(repeatCount)}
    </div>
  );
};

export default Tags;
