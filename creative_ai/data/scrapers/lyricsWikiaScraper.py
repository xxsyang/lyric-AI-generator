#!/usr/bin/env python
# -*- coding: utf-8 -*-
from baseScraper import *


class LyricsWikiaScraper(BaseScraper):

    def __init__(self):
        """
        This is the constructor for the LyricsWikiaScraper.
        It sets the values for specific data needed for the scraper.
        """
        self.hostUrl = "lyrics.fandom.com"
        self.generalArtistPath = "/wiki/" # note: case matters
        self.spaceChar = "_"
        self.delay = 1.0

    def artistExistsOnSite(self, html):
        """
        Returns True if the string "This page needs content" is not
        present in the HTML.
        """
        return "This page needs content" not in html

    def capitalizeName(self, artist, delimiter):
        """
        Returns a string of the name of an artist with the first letter of
        each part of the name capitalized.
        For example: bob dylan -> Bob Dylan
        """
        name = artist.split(delimiter)
        for i in range(len(name)):
            name[i] = name[i].capitalize()

        return delimiter.join(name)

    def constructArtistUrlSuffix(self, artist):
        """
        Returns the relative path to the artist's page on the website.
        For example: /wiki/Category:Songs_by_Katy_Perry
        """
        artist = self.capitalizeName(artist, self.spaceChar)
        return self.generalArtistPath + artist

    def isolateNextPageUrl(self, html):
        """
        Gets the url of the next page for the artist.
        """
        matchRegex = re.compile('previous 200.*?href="(.*?)".*?next 200')
        relativeUrl = re.findall(matchRegex, html)
        if not relativeUrl:
            return ""
        return relativeUrl[0]

    def getSongUrls(self, html):
        """
        Returns a dictionary of {song title: relative URL}.
        Gets the table of links to song pages and parses them
        accordingly.
        For example: { "Teenage_Dream": "/wiki/Katy_Perry:Teenage_Dream" }
        """
        #print(html)
        startString = "mw-headline"
        endString = "Artist Information"
        startIndex = html.find(startString)

        # the 2nd parameter is the starting index for the search for endString
        endIndex = html.find(endString)
        table = html[startIndex:endIndex]
        urls = table.split('href="')
        #print(urls[4])

        urlByTitle = {}
        for url in urls[2:]:
            try:
                if ("title=\"" in url) and ("/wiki/" in url) and (":" in url) and ("Category" not in url) and ("https" not in url):
                    title_url_index = url.find("\"")
                    title_url = url[:title_url_index]
                    titlekinda = title_url[6:]
                    #print(titlekinda, title_url)
                    urlByTitle[titlekinda] = title_url
            except:
                pass
        #import json
        #print(json.dumps(urlByTitle, indent=4, sort_keys=True))
        return urlByTitle

    def getSongUrlsWithPagination(self, html):
        """
        Gets song urls for artist pages that have pagination,
        i.e. links to the next page and the previous page.
        """
        urlByTitle = {}
        nextPageUrl = self.isolateNextPageUrl(html)
        while nextPageUrl != "":
            nextPageHtml = self.getPageHtml(nextPageUrl)
            urlByTitle.update(self.getSongUrls(nextPageHtml))
            nextPageUrl = self.isolateNextPageUrl(nextPageHtml)

        return urlByTitle

    def getSongLyrics(self, html):
        """
        Returns a single string of the lyrics for the song specified
        in the html.
        Gets an approximation of where the lyrics begin, then finds the
        exact start after skipping any Javascript. Gets an exact end for
        the lyrics by finding an HTML comment.
        This website has lyric characters given in HTML ASCII values
        (i.e. &#89; for Y), so the loop deals with converting those values
        into Python strings via ASCII lookup. Note that some lyrics
        contain symbols, blank lines, or HTML tags such as <i>.
        The loop attempts to mitigate this.
        """
        # apparently lyricsWikia has updated their site and now
        # lyrics begin in a div with class lyricbox
        exactStart = '<div class=\'lyricbox\'>'
        startIndex = html.find(exactStart) + len(exactStart)

        exactEnd = "<!--"
        endIndex = html.find(exactEnd, startIndex)
        lyricLines = html[startIndex:endIndex].split("<br")

        lyricsString = ""
        totalLines = []
        MAX_ASCII = 256 # maximum integer value in the ascii table
        for i in range(len(lyricLines)):
            lyricsString = ""
            if "&" in lyricLines[i]: # avoid processing blank lines
                contentStart = lyricLines[i].find("&")
                lyricLines[i] = lyricLines[i][contentStart:]

                asciiValues = lyricLines[i].split(";")[:-1]
                for value in asciiValues:
                    integerStart = value.find("#") + 1
                    asciiString = value[integerStart:]
                    if asciiString.isdigit() and int(asciiString) <= MAX_ASCII:
                        character = chr(int(asciiString))
                        lyricsString += character
            lyricsString += "\n"
            totalLines.append(lyricsString)
        totalLines[-1] = totalLines[-1][:-20]
        return totalLines

    def saveLyrics(self, title, relativeUrl, dirName):
        """
        Saves the lyrics for the song at self.hostUrl + relativeUrl to
        the directory specified by dirName in a file called <title>.txt.
        """
        html = self.getPageHtml(relativeUrl, True)
        #print(html)
        lyrics = self.getSongLyrics(html)
        title = re.sub("/", "_", title)
        for encoding in URL_ENCODINGS:
            title = re.sub(encoding, URL_ENCODINGS[encoding], title)
        lyricsFileName = (dirName + "/" + title + ".txt")
        lyricsFile = codecs.open(lyricsFileName, "w", "utf-8", errors = "ignore")
        for line in lyrics:
            lyricsFile.write(line)

    def scrape(self, artist):
        """
        Prompts user for artist input.
        Gets all available song lyrics for the artist <artist>
        and saves each individual song to the data/music/<artist>
        folder in a file called <title>.txt.
        """
        formattedArtistName = re.sub(" ", self.spaceChar, artist)
        artistUrlSuffix = self.constructArtistUrlSuffix(formattedArtistName) #/wiki/katy_perry
        artistFirstPageHtml = self.getPageHtml(artistUrlSuffix, True)

        if not self.artistExistsOnSite(artistFirstPageHtml):
            print("\nThe artist", formattedArtistName, "does not exist on ", end="")
            print(self.hostUrl, "at", artistUrlSuffix)
            print("If you think this artist should exist on this site, ", end="")
            print("try checking for capitalization or spelling errors")
            return

        urlByTitle = self.getSongUrls(artistFirstPageHtml)

        # get all the next pages, if they exist, and add them to url list
        #paginatedUrls = self.getSongUrlsWithPagination(artistFirstPageHtml)
        #urlByTitle.update(paginatedUrls)

        #print(self.hostUrl)
        print("\nFound", len(urlByTitle), "songs by", formattedArtistName, end="")
        print(" with lyrics at", self.hostUrl)

        # make artistDir (data/music/<artist>) and then save files of
        # song lyrics to that directory
        # scriptDir is the absolute path to this script, baseScraper.py
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        artistDir = os.path.join(scriptDir, '../lyrics', \
                                 re.sub(" ", "_", artist))

        # avoid remaking an existing directory
        if not os.path.exists(artistDir):
            os.makedirs(artistDir)

        for title in tqdm(urlByTitle, total=len(urlByTitle), desc="Saving lyrics", ncols=80):
            self.saveLyrics(title, urlByTitle[title], artistDir)

        print("\nLyrics acquired from", self.hostUrl)


if __name__ == "__main__":
    scraper = LyricsWikiaScraper()
    artist = input("Enter the name of the artist you wish to search for: ")
    scraper.scrape(artist)
    # scrapers gonna scrape, scrape, scrape, scrape, scrape
