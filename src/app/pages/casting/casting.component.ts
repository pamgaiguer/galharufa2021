import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-casting',
  templateUrl: './casting.component.html',
  styleUrls: ['./casting.component.scss']
})
export class CastingComponent implements OnInit {
  sectionTitle = 'castingTitle';
  images = [62, 83, 466, 965, 982, 1043].map(n => `https://picsum.photos/id/${n}/410/515?grayscale`);

  constructor() {}

  ngOnInit(): void {}
}
