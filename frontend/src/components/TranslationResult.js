import React from 'react';

const TranslationResult = ({ translatedText }) => {
    return (
        <div>
            <h3>Translated Text:</h3>
            <p>{translatedText}</p>
        </div>
    );
};

export default TranslationResult;
