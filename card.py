import streamlit.components.v1 as com

def card(name, url, price, subs, level):
  for i in range(len(price)):
    if price[i] == 0:
        price[i] = 'Free'

  com.html(f"""
<div class="ag-format-container">
  <div class="ag-courses_box">
    <div class="ag-courses_item">
      <a href="{url[0]}" class="ag-courses-item_link" target="_blank">
        <div class="ag-courses-item_bg"></div>

        <div class="ag-courses-item_title">
          {name[0]}
        </div>
        <div class="ag-courses-item_date-box">
          Level: {level[0]}
        </div>
        <div class="ag-courses-item_date-box">
          Subscribers: {subs[0]}
        </div>
        <div class="ag-courses-item_date-box">
          Price:
          <span class="ag-courses-item_date">
            $ {price[0]}
          </span>
        </div>
      </a>
    </div>

    <div class="ag-courses_item">
      <a href="{url[1]}" class="ag-courses-item_link">
        <div class="ag-courses-item_bg"></div>

        <div class="ag-courses-item_title">
          {name[1]}
        </div>
        <div class="ag-courses-item_date-box">
          Level: {level[1]}
        </div>
        <div class="ag-courses-item_date-box">
          Subscribers: {subs[1]}
        </div>
        <div class="ag-courses-item_date-box">
          Price:
          <span class="ag-courses-item_date">
            $ {price[1]}
          </span>
        </div>
      </a>
    </div>

    <div class="ag-courses_item">
      <a href="{url[2]}" class="ag-courses-item_link">
        <div class="ag-courses-item_bg"></div>

        <div class="ag-courses-item_title">
          {name[2]}
        </div>
        <div class="ag-courses-item_date-box">
        Level: {level[2]}
        </div>
        <div class="ag-courses-item_date-box">
          Subscribers: {subs[2]}
        </div>
        <div class="ag-courses-item_date-box">
          Price: 
          <span class="ag-courses-item_date">
            $ {price[2]}
          </span>
        </div>
      </a>
    </div>

    <div class="ag-courses_item">
      <a href="{url[3]}" class="ag-courses-item_link">
        <div class="ag-courses-item_bg"></div>

        <div class="ag-courses-item_title">
          {name[3]}
        </div>
        <div class="ag-courses-item_date-box">
          Level: {level[3]}
        </div>
        <div class="ag-courses-item_date-box">
          Subscribers: {subs[3]}
        </div>
        <div class="ag-courses-item_date-box">
          Price:
          <span class="ag-courses-item_date">
            $ {price[3]}
          </span>
        </div>
      </a>
    </div>

    <div class="ag-courses_item">
      <a href="{url[4]}" class="ag-courses-item_link">
        <div class="ag-courses-item_bg"></div>

        <div class="ag-courses-item_title">
          {name[4]}
        </div>
          <div class="ag-courses-item_date-box">
            Level: {level[4]}
          </div>
          <div class="ag-courses-item_date-box">
            Subscribers: {subs[4]}
          </div>
        <div class="ag-courses-item_date-box">
          Price:
          <span class="ag-courses-item_date">
            $ {price[4]}
          </span>
        </div>
      </a>
    </div>

    <div class="ag-courses_item">
      <a href="{url[5]}" class="ag-courses-item_link">
        <div class="ag-courses-item_bg"></div>

        <div class="ag-courses-item_title">
          {name[5]}
        </div>
        <div class="ag-courses-item_date-box">
        Level: {level[5]}
        </div>
        <div class="ag-courses-item_date-box">
          Subscribers: {subs[5]}
        </div>
        <div class="ag-courses-item_date-box">
          Price:
          <span class="ag-courses-item_date">
            $ {price[5]}
          </span>
        </div>
      </a>
    </div>

  </div>
</div>
    """+"""
    <style>
    .ag-format-container {
    width: 1142px;
    margin: 0 auto;
  }
  
  
  body {
    background-color: #0e1117;
  }
  .ag-courses_box {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    font-family: 'Source Sans Pro', sans-serif;
  
    padding: 50px 0;
  }
  .ag-courses_item {
    -ms-flex-preferred-size: calc(33.33333% - 30px);
    flex-basis: calc(33.33333% - 30px);
  
    margin: 0 15px 30px;
  
    overflow: hidden;
  
    border-radius: 28px;
  }
  .ag-courses-item_link {
    display: block;
    padding: 30px 20px;
    background-color: #131720;
  
    overflow: hidden;
  
    position: relative;
  }
  .ag-courses-item_link:hover,
  .ag-courses-item_link:hover .ag-courses-item_date {
    text-decoration: none;
    color: #FFF;
  }
  .ag-courses-item_link:hover .ag-courses-item_bg {
    -webkit-transform: scale(10);
    -ms-transform: scale(10);
    transform: scale(10);
  }
  .ag-courses-item_title {
    min-height: 87px;
    margin: 0 0 25px;
  
    overflow: hidden;
  
    font-weight: bold;
    font-size: 30px;
    color: #FFF;
  
    z-index: 2;
    position: relative;
  }
  .ag-courses-item_date-box {
    font-size: 30px;
    color: #FFF;
  
    z-index: 2;
    position: relative;
  }
  .ag-courses-item_date {
    font-weight: bold;
    color: #f9b234;
  
    -webkit-transition: color .5s ease;
    -o-transition: color .5s ease;
    transition: color .5s ease
  }
  .ag-courses-item_bg {
    height: 128px;
    width: 128px;
    background-color: #f9b234;
  
    z-index: 1;
    position: absolute;
    top: -75px;
    right: -75px;
  
    border-radius: 50%;
  
    -webkit-transition: all .5s ease;
    -o-transition: all .5s ease;
    transition: all .5s ease;
  }
  
  
.ag-courses_item:nth-child(2n) .ag-courses-item_bg {
  background-color: #3ecd5e;
}
.ag-courses_item:nth-child(3n) .ag-courses-item_bg {
  background-color: #e44002;
}
.ag-courses_item:nth-child(4n) .ag-courses-item_bg {
  background-color: #952aff;
}
.ag-courses_item:nth-child(5n) .ag-courses-item_bg {
  background-color: #cd3e94;
}
.ag-courses_item:nth-child(6n) .ag-courses-item_bg {
  background-color: #4c49ea;
}
  
  @media only screen and (max-width: 979px) {
    .ag-courses_item {
      -ms-flex-preferred-size: calc(50% - 30px);
      flex-basis: calc(50% - 30px);
    }
    .ag-courses-item_title {
      font-size: 24px;
    }
  }
  
  @media only screen and (max-width: 767px) {
    .ag-format-container {
      width: 96%;
    }
  
  }
  @media only screen and (max-width: 639px) {
    .ag-courses_item {
      -ms-flex-preferred-size: 100%;
      flex-basis: 100%;
    }
    .ag-courses-item_title {
      min-height: 72px;
      line-height: 1;
  
      font-size: 24px;
    }
    .ag-courses-item_link {
      padding: 22px 40px;
    }
    .ag-courses-item_date-box {
      font-size: 22px;
    }
  }
  </style>
""",
  height=1282,
  width=560)