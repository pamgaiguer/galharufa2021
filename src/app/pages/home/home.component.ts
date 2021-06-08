import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  images = [62, 83, 466, 965, 982, 1043, 738].map(n => `https://picsum.photos/id/${n}/1024/768?grayscale`);

  constructor() {}

  ngOnInit(): void {}
}
