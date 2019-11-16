import React from 'react';
import 'rc-slider/assets/index.css';
import Moment from 'moment';
import Slider from 'rc-slider';

const startingDate = Moment("1996-1-1");
const amountOfImages = 366;
const autoplayTimeout = 50;

const imagenameprefixes = [
    "t2m_in_temp_doy_",
];

class App extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            imageNumber: 1,
            autoplayEnabled: false,
        };
        setInterval(this.handleAutoplayTimeout.bind(this), autoplayTimeout);
    }

    render() {
        return (
            <div className="App">
                <div className="slider">
                    <Slider onChange={this.scrollImage.bind(this)} min={1} max={amountOfImages} value={this.state.imageNumber}/>
                </div>
                <div onClick={this.toggleAutoplay.bind(this)}>
                    {
                        imagenameprefixes.map((imageprefix) =>
                            <img src={`/images/${imageprefix}${this.prefixedImgNr()}.png`} alt="something" />
                        )
                    }

                </div>

                <span className="metadata">
                    {Moment(startingDate).add(this.state.imageNumber - 1, "day").format("DD MMM YYYY")}
                </span>
            </div>
        );
    }

    toggleAutoplay() {
        this.setState({
            autoplayEnabled: !this.state.autoplayEnabled,
        });
    }

    handleAutoplayTimeout() {
        if(this.state.autoplayEnabled && this.state.imageNumber < amountOfImages)
            this.setState((prevState) => {
                return {
                    imageNumber: prevState.imageNumber+1,
                    autoplayEnabled: prevState.imageNumber+1 < amountOfImages
                }
            });
    }

    scrollImage(newImageNumber){
        this.setState({
            imageNumber: newImageNumber
        })
    }

    prefixedImgNr(){
        return ('' + this.state.imageNumber).padStart(5, '0');
    }
}

export default App;
