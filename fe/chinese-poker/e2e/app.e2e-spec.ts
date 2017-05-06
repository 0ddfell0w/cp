import { ChinesePokerPage } from './app.po';

describe('chinese-poker App', function() {
  let page: ChinesePokerPage;

  beforeEach(() => {
  page = new ChinesePokerPage();
  });

  it('should display message saying app works', () => {
  page.navigateTo();
  expect(page.getParagraphText()).toEqual('app works!');
  });
});
